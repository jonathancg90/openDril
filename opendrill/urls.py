from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = patterns('',


    #Client
    url(r'^client/', include('apps.mail.urls.client')),

    #Admin
    url(r'^admin/', include('apps.mail.urls.admin')),

    #Website
    url(r'^', include('apps.mail.urls')),
)
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT}))