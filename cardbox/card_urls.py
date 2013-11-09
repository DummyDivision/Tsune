from django.conf.urls import patterns, url
from cardbox import card_views

urlpatterns = patterns('',
                       url(r'^new$', card_views.CardCreate.as_view(
                           template_name="cardbox/card/card_form.html"),
                           name='card_new'),
                       url(r'^edit/(?P<pk>\d+)$', card_views.CardUpdate.as_view(
                           template_name="cardbox/card/card_form.html"), name='card_edit'),
                       url(r'^delete/(?P<pk>\d+)$', card_views.CardDelete.as_view(
                           template_name="cardbox/card/card_confirm_delete.html"),
                           name='card_delete'),
                       url(r'^detail/(?P<pk>\d+)/$', card_views.CardDetailView.as_view(
                           template_name="cardbox/card/card_detail.html"), name='card_detail')
)
