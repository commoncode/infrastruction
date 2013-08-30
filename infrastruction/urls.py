from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^grappelli/', include('grappelli.urls')),

)

#
# DEBUG MEDIA SETTINGS - Django Serves Static for us, but we must serve Media
#

if hasattr(settings, 'SERVE_MEDIA') and settings.SERVE_MEDIA:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += patterns('django.views.static',
        url(r'^media/(?P<path>.*)$',
            'serve',
            { 'document_root': settings.MEDIA_ROOT, },
        ),
    ) + staticfiles_urlpatterns()
