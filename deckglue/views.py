from __future__ import division
import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from cardbox.deck_views import DeckList
from deckglue.models import DelayablePractice
from memorize.models import Practice
from memorize.algorithm import interval
from cardbox.card_model import Card
from django.utils.timezone import utc
from cardbox.card_views import CardUpdate

class PracticeDeckList(DeckList):
    """Adds due cards to DeckList overview.

    This is an extension of :class:`tsune.cardbox.deck_views.DeckList` which overwrites
    the get_queryset function to add the number of due cards and due percentage to
    the deck view.

    """
    def get_queryset(self):
        deck_list = super(PracticeDeckList,self).queryset()
        all_due_cards_for_user = DelayablePractice.objects.filter(next_practice__lte = datetime.datetime.utcnow().replace(tzinfo=utc), user=self.request.user)
        for deck in deck_list:
            card_ids = Card.objects.filter(deck=deck).values_list("ID", flat=True)
            deck.due_cards = all_due_cards_for_user.filter(object_id__in=card_ids).count()
            try:
                deck.due_percentage = (deck.due_cards/deck.get_total_cards()) * 100
            except ZeroDivisionError:
                deck.due_percentage = 0
            deck.not_due = 100 - deck.due_percentage
        return deck_list

class PracticeCardUpdate(CardUpdate):
    """Enables Editing from Learning View.

    This is an extension of the :class:`tsune.cardbox.card_views.CardUpdate` which
    overwrites the get_success_url function to return to the right site if the editing
    is started from the learning view as opposed to the decklist view.

    """
    def get_success_url(self):
        if 'learning' in self.request.GET:
            # Shows answers on return
            return reverse('learning:learning', args=( self.kwargs.get('deck_id'),))+"?showAnswer=true"
        else:
            return super(PracticeCardUpdate,self).get_success_url()

class next_practice_item(TemplateView):


    def get(self, request, *args, **kwargs):
        """Prepares the items to learn and sorts them differently depending on mode.

         If the user chooses force mode the cards will be displayed according to when he last viewed them starting
         with the least recent. If the user uses Skip in this mode, the card will be put at the end of the deck.

        """
        all_card_ids_for_deck = Card.objects.filter(deck=kwargs.get('deck_id')).values_list("ID", flat=True)
        # Force mode activation. TODO: Let the user actually choose it somewhere.
        if not 'force' in kwargs:
            kwargs['force'] = False
        if kwargs['force']:
            all_practice_for_this_deck = Practice.objects.filter(user=self.request.user, object_id__in=all_card_ids_for_deck).order_by('ended_last_viewing')
        else:
            all_practice_for_this_deck = Practice.objects.filter(next_practice__lte=datetime.datetime.utcnow().replace(tzinfo=utc), user=self.request.user, object_id__in=all_card_ids_for_deck).order_by('next_practice')
        if len(all_practice_for_this_deck) is 0:
            return HttpResponseRedirect("/comic/")
        else:
            kwargs['practice'] = all_practice_for_this_deck[0]
            return super(next_practice_item,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        """ Prepares the practice item and sets the started_last_viewing of the practice model.

        It also calculates the time which each choice of difficulty will add. Should be changed
        if the time calculating algorithm changes.

        """
        context = super(next_practice_item, self).get_context_data(**kwargs)
        context['id'] =  kwargs['practice'].id
        context['object'] = kwargs['practice'].item
        context['easy_time'] = interval(kwargs['practice'].times_practiced,5,kwargs['practice'].easy_factor)[0]
        context['normal_time'] = interval(kwargs['practice'].times_practiced,3,kwargs['practice'].easy_factor)[0]
        context['hard_time'] = interval(kwargs['practice'].times_practiced,1,kwargs['practice'].easy_factor)[0]
        context['force'] = kwargs['force']
        kwargs['practice'].started_last_viewing = datetime.datetime.utcnow().replace(tzinfo=utc)
        kwargs['practice'].save()
        return context

@login_required
def process_rating(request):
    """Processes the rating if any given and links back to the learning method of the current deck.

    """

    practice_item = get_object_or_404(DelayablePractice,
                                      pk=int(request.POST['id']))
    if request.POST['force'] == 'False':
        rating = int(request.POST['rating_value'])
        if rating < 2:
            practice_item.delay(10)
        elif rating == 2:
            practice_item.delay(30)
            practice_item.times_practiced += 1
        else:
            practice_item.set_next_practice(rating)

    practice_item.ended_last_viewing = datetime.datetime.utcnow().replace(tzinfo=utc)
    practice_item.save()
    return HttpResponseRedirect(reverse('learning:learning', args=(practice_item.item.deck_id,)))