# coding=utf-8
from django.contrib.localflavor import kw

from django.http.response import HttpResponseForbidden
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from guardian.shortcuts import assign_perm
from guardian.shortcuts import get_objects_for_user
from cardbox.deck_forms import DeckForm
from cardbox.deck_model import Deck

class DeckList(ListView):
    def queryset(self):
        return get_objects_for_user(self.request.user, 'cardbox.view_deck')

class DeckCreate(CreateView):
    model = Deck
    form_class = DeckForm
    success_url = reverse_lazy('deck:deck_list')

    def form_valid(self, form):
        created_deck = form.save(commit=False)
        created_deck.save()
        creator = self.request.user
        # Assign default permissions to the creator of the deck.
        assign_perm('cardbox.view_deck', creator, created_deck)
        assign_perm('cardbox.change_deck', creator, created_deck)
        assign_perm('cardbox.delete_deck', creator, created_deck)
        return super(CreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(DeckCreate, self).get_context_data(**kwargs)
        context['action'] = "erstellen"
        context['button_text'] = "Erstellen"
        return context


class DeckDetailView(DetailView):
    model = Deck


class DeckUpdate(UpdateView):
    model = Deck
    form_class = DeckForm
    success_url = reverse_lazy('deck:deck_list')

    def get_context_data(self, **kwargs):
        context = super(DeckUpdate, self).get_context_data(**kwargs)
        context['action'] = "bearbeiten"
        context['button_text'] = "Änderungen übernehmen"
        return context


class DeckDelete(DeleteView):
    model = Deck
    success_url = reverse_lazy('deck:deck_list')
    
    def get(selfself, request, *args, **kwargs):
        """Never get the confirm_delete template!"""
        print "test"
        return HttpResponseForbidden("<h1>Access denied</h1>")

    def post(self, *args, **kwargs):
        return super(DeckDelete, self).post(self, args, kwargs)