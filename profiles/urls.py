from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
import views

urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)/$',
                           login_required(views.ProfileView.as_view(
                               template_name="profiles/profile/profile.html")), name='profile_detail')
)