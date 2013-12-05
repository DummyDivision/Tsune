from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from .views import PracticeDeckList
from cardbox import deck_views

urlpatterns = patterns('',
                     url(r'^$',login_required(PracticeDeckList.as_view(template_name="cardbox/deck/deck_list.html")),
                         name='deck_list'),
                     url(r'^new$', login_required(deck_views.DeckCreate.as_view(
                           template_name="cardbox/deck/deck_form.html")), name='deck_new'),
                       url(r'^edit/(?P<pk>\d+)$', login_required(deck_views.DeckUpdate.as_view(
                           template_name="cardbox/deck/deck_form.html")), name='deck_edit'),
                       url(r'^delete/(?P<pk>\d+)$', login_required(deck_views.DeckDelete.as_view(
                           template_name="cardbox/deck/deck_confirm_delete.html")),
                           name='deck_delete'),
                       url(r'^detail/(?P<pk>\d+)/$', login_required(
                           deck_views.DeckDetailView.as_view(
                               template_name="cardbox/deck/deck_detail.html")), name='deck_detail')
)