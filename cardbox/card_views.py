# coding=utf-8
# TODO: user authentification
# TODO: comments
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from cardbox.card_forms import CardForm

from cardbox.card_model import Card


class CardCreate(CreateView):
    model = Card
    form_class = CardForm
    def get_context_data(self, **kwargs):
        context = super(CardCreate, self).get_context_data(**kwargs)
        context['action'] = "erstellen"
        context['button_text'] = "Erstellen"
        return context

class CardUpdate(UpdateView):
    model = Card
    form_class = CardForm
    def get_context_data(self, **kwargs):
        context = super(CardUpdate, self).get_context_data(**kwargs)
        context['action'] = "bearbeiten"
        context['button_text'] = "Änderungen Übernehmen"
        return context
class CardDelete(DeleteView):
    model = Card
    def get(self, request, *args, **kwargs):
        """Never get the confirm_delete template!"""
        print "test"
        return HttpResponseForbidden("<h1>Access Denied</h1>")

    def post(self, *args, **kwargs):
        #TODO: user authentification
        return super(CardDelete, self).post(self, args, kwargs)

