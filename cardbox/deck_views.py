# coding=utf-8
# TODO: User authentication
from django.contrib.localflavor import kw

from django.http import HttpResponse
from django.http.response import HttpResponseForbidden
from django.template import context
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from cardbox.deck_forms import DeckForm
from cardbox.deck_model import Deck

class DeckList(ListView):
    model = Deck


class DeckCreate(CreateView):
    model = Deck
    form_class = DeckForm
    success_url = reverse_lazy('deck:deck_list')

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
        # TODO: user authentication
        return super(DeckDelete, self).post(self, args, kwargs)