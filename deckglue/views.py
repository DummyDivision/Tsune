from __future__ import division
import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from cardbox.deck_views import DeckList
from memorize.models import Practice
from memorize.algorithm import interval
from cardbox.card_model import Card
from django.utils.timezone import utc
from cardbox.card_views import CardUpdate

class PracticeDeckList(DeckList):
    """Adds due cards to DeckList overview.

    """
    def get_queryset(self):
        deck_list = super(PracticeDeckList,self).queryset()
        all_due_cards_for_user = Practice.objects.filter(next_practice__lte = datetime.datetime.utcnow().replace(tzinfo=utc), user=self.request.user)
        for deck in deck_list:
            card_ids = Card.objects.filter(deck=deck).values_list("ID", flat=True)
            deck.due_cards = all_due_cards_for_user.filter(object_id__in=card_ids).count()
            try:
                deck.due_percentage = (deck.due_cards/deck.get_total_cards()) * 100
            except ZeroDivisionError:
                deck.due_percentage = 0
            deck.not_due = 100 - deck.due_percentage
            print deck.due_percentage
            print deck.not_due
            print deck.due_cards
            print deck.get_total_cards()
        return deck_list

class PracticeCardUpdate(CardUpdate):
    """Enables Editing from Learning View.

    """
    def get_success_url(self):
        if 'learning' in self.request.GET:
            #Shows answers on return
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

        #Force mode activation. TODO: Let the user actually choose it somewhere.
        kwargs['force'] = False
        if kwargs['force']:
            all_practice_for_this_deck = Practice.objects.filter(user=self.request.user, object_id__in=all_card_ids_for_deck).order_by('ended_last_viewing')
        else:
            all_practice_for_this_deck = Practice.objects.filter(next_practice__lte=datetime.datetime.utcnow().replace(tzinfo=utc), user=self.request.user, object_id__in=all_card_ids_for_deck).order_by('next_practice')
        if len(all_practice_for_this_deck) is 0:
            return render(self.request, template_name="learning/learn_done.html")
        else:
            kwargs['practice'] = all_practice_for_this_deck[0]
            return super(next_practice_item,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        """ Prepares the practice item and sets the started_last_viewing of the practice model.

        """
        context = super(next_practice_item, self).get_context_data(**kwargs)
        context['id'] =  kwargs['practice'].id
        context['object'] = kwargs['practice'].item
        context['easy_time'] = interval(kwargs['practice'].times_practiced,4,2.5)[0]
        context['normal_time'] = interval(kwargs['practice'].times_practiced,2,2.5)[0]
        context['hard_time'] = interval(kwargs['practice'].times_practiced,0,2.5)[0]
        context['force'] = kwargs['force']
        kwargs['practice'].started_last_viewing = datetime.datetime.utcnow().replace(tzinfo=utc)
        kwargs['practice'].save()
        return context

@login_required
def process_rating(request):
    """Processes the rating if any given and links back to the learning method of the current deck.

    """

    practice_item = get_object_or_404(Practice,
                                      pk=int(request.POST['id']))
    print request.POST
    if request.POST['force'] == 'False':
        rating = int(request.POST['rating_value'])
        print rating
        if rating == -1:
            practice_item.delay()
        elif rating >= 0 and rating <= 4:
            practice_item.set_next_practice(rating)
    else:
        #Updating times practiced since it normally gets updated in set_next_practice
        practice_item.times_practiced += 1
    practice_item.ended_last_viewing = datetime.datetime.utcnow().replace(tzinfo=utc)
    practice_item.save()
    return HttpResponseRedirect(reverse('learning:learning', args=(practice_item.item.deck_id,)))