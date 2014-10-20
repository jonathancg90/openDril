from django.conf.urls import patterns, url

from apps.mail.views.List import ListTemplateView
from apps.mail.views.List import ListCreateView
from apps.mail.views.List import ListUpdateView
from apps.mail.views.List import ListDeleteView


urlpatterns = patterns('',
                       url(r'^$',
                           ListTemplateView.as_view(),
                           name='list_view'),
                       url(r'^create/$',
                           ListCreateView.as_view(),
                           name='list_create_view'),
                       url(r'^update/(?P<pk>\d+)/$',
                           ListUpdateView.as_view(),
                           name='list_update_view'),
                       url(r'^delete/$',
                           ListDeleteView.as_view(),
                           name='list_delete_view'),
                       )