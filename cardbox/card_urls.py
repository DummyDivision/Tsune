from django.conf.urls import patterns, url
from cardbox import card_views

urlpatterns = patterns('',
                       url(r'^(?P<deck_id>\d+)$',
                           card_views.CardList.as_view(template_name="cardbox/card/card_list.html"),
                           name='card_list'),
                       url(r'^(?P<deck_id>\d+)/new$', card_views.CardCreate.as_view(
                           template_name="cardbox/card/card_form.html"),
                           name='card_new'),
                       url(r'^(?P<deck_id>\d+)/edit/(?P<pk>\d+)$', card_views.CardUpdate.as_view(
                           template_name="cardbox/card/card_form.html"), name='card_edit'),
                       url(r'^(?P<deck_id>\d+)/delete/(?P<pk>\d+)$', card_views.CardDelete.as_view(
                           template_name="cardbox/card/card_confirm_delete.html"),
                           name='card_delete'),
                       url(r'^(?P<deck_id>\d+)/detail/(?P<pk>\d+)/$', card_views.CardDetailView.as_view(
                           template_name="cardbox/card/card_detail.html"), name='card_detail')
)
