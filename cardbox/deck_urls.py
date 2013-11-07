from django.conf.urls import patterns, include, url
import deck_views


urlpatterns = patterns('',
                       url(r'^$', deck_views.index, name='index'),
)
