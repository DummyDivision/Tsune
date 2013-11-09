from django.conf.urls import patterns, url
from cardbox import card_views

urlpatterns = patterns('',
                       url(r'^delete/(?P<pk>\d+)$', card_views.CardDelete.as_view(
                           template_name="cardbox/card/card_confirm_delete.html"),
                           name='card_delete'),
)
