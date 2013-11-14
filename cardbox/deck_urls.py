from django.conf.urls import patterns, include, url
import deck_views


urlpatterns = patterns('',
                       url(r'^$',
                           deck_views.DeckList.as_view(template_name="cardbox/deck/deck_list.html"),
                           name='deck_list'),
                       url(r'^new$', deck_views.DeckCreate.as_view(
                           template_name="cardbox/deck/deck_form.html"), name='deck_new'),
                       url(r'^edit/(?P<pk>\d+)$', deck_views.DeckUpdate.as_view(
                           template_name="cardbox/deck/deck_form.html"), name='deck_edit'),
                       url(r'^delete/(?P<pk>\d+)$', deck_views.DeckDelete.as_view(
                           template_name="cardbox/deck/deck_confirm_delete.html"),
                           name='deck_delete'),
                       url(r'^detail/(?P<pk>\d+)/$', deck_views.DeckDetailView.as_view(
                           template_name="cardbox/deck/deck_detail.html"), name='deck_detail')
)
