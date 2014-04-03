from django.conf.urls import patterns, include, url
from authentication import views

urlpatterns = patterns('django.contrib.auth.views',

    url(r'^login/$', views.login, {'template_name': 'authentication/login.html'}),
    url(r'^logout/$', 'logout_then_login',name='logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls')))