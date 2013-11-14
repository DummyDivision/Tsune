# coding=utf-8
# TODO: user authentification
# TODO: comments
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from cardbox.card_forms import CardForm

from cardbox.card_model import Card
from cardbox.deck_model import Deck

class CardList(ListView):
    model = Card

    def get_queryset(self):
        deck = get_object_or_404(Deck, ID__iexact=self.kwargs.get('deck_id'))
        return Card.objects.filter(deck=deck)

    def get_context_data(self, **kwargs):
        context = super(CardList, self).get_context_data(**kwargs)
        context['deck_id'] = self.kwargs.get('deck_id')
        return context

class CardCreate(CreateView):
    model = Card
    form_class = CardForm

    def get_success_url(self):
            return reverse_lazy('card:card_list',  kwargs={'deck_id': self.kwargs.get('deck_id')})

    def get_context_data(self, **kwargs):
        context = super(CardCreate, self).get_context_data(**kwargs)
        context['action'] = "erstellen"
        context['button_text'] = "Erstellen"
        context['deck_id'] = self.kwargs.get('deck_id')
        return context


class CardDetailView(DetailView):
    model = Card

    def get_context_data(self, **kwargs):
        context = super(CardDetailView, self).get_context_data(**kwargs)
        return context

class CardUpdate(UpdateView):
    model = Card
    form_class = CardForm
    def get_success_url(self):
        return reverse_lazy('card:card_list',  kwargs={'deck_id': self.kwargs.get('deck_id')})

    def get_context_data(self, **kwargs):
        context = super(CardUpdate, self).get_context_data(**kwargs)
        context['action'] = "bearbeiten"
        context['button_text'] = "Änderungen Übernehmen"
        context['deck_id'] = self.kwargs.get('deck_id')
        return context


class CardDelete(DeleteView):
    model = Card
    def get_success_url(self):
        return reverse_lazy('card:card_list',  kwargs={'deck_id': self.kwargs.get('deck_id')})

    def get(self, request, *args, **kwargs):
        """Never get the confirm_delete template!"""
        print "test"
        return HttpResponseForbidden("<h1>Access Denied</h1>")

    def post(self, *args, **kwargs):
        #TODO: user authentification
        return super(CardDelete, self).post(self, args, kwargs)



