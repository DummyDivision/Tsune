from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
import views

urlpatterns = patterns('',
                       url(r'^$',
                           login_required(views.upload_file), name='upload')
)