from django.conf.urls import patterns, include, url

urlpatterns = patterns('django.contrib.auth.views',

    url(r'^login/$', 'login', {'template_name': 'authentication/login.html'}),
    url(r'^logout/$', 'logout_then_login'))