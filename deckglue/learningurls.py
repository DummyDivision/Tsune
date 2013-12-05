from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from .views import process_rating
from .views import next_practice_item

urlpatterns = patterns('',
                       url(r'^(?P<deck_id>\d+)/$',
                           login_required(next_practice_item.as_view(
                               template_name="learning/learn_item.html")), name='learning'),
                       url(r'^rate$',
                           process_rating, name='learning_post'),
)
