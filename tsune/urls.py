from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tsune.views.home', name='home'),
    # url(r'^tsune/', include('tsune.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:go.contrib.admindocs.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^cardbox/deck/', include('cardbox.deck_urls', namespace="deck")),
    url(r'^cardbox/card/', include('cardbox.card_urls', namespace="card")),
)
