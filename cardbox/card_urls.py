from django.conf.urls import patterns, include, url
import card_views

urlpatterns = patterns('',
                       url(r'^$', card_views.index, name='index'),
)
