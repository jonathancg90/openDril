from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',

    url(r'^', include('mail.urls')),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT}))