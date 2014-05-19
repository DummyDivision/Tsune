from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.http import HttpResponseRedirect

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tsune.views.home', name='home'),
    # url(r'^tsune/', include('tsune.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:go.contrib.admindocs.urls')),

    url(r'^$', lambda x: HttpResponseRedirect('/cardbox/')),  # redirect to /cardbox/
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cardbox/', include('deckglue.deckurls', namespace="deck")),
    url(r'^user/', include('authentication.urls')),
    url(r'^learning/', include('deckglue.learningurls', namespace="learning")),
    url(r'^cardbox/cards/', include('deckglue.cardurls', namespace="card")),
    url(r'^markitup/', include('markitup.urls')),
    url(r'^profile/', include('profiles.urls', namespace="profile")),
    url(r'^inplaceeditform/', include('inplaceeditform.urls')),
    url(r'^upload/', include('upload.urls', namespace="upload")),
    url(r'^comic/', include('comic.urls'))
)
