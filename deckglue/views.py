# Create your views here.
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