from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

import views


urlpatterns = patterns('',
                       url(r'^$',
                           login_required(views.ComicView.as_view(
                               template_name="comic/comic.html")), name='comic')
)