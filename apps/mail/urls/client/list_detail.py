from django.conf.urls import patterns, url

from apps.mail.views.client.DetailList import ListDetailView
from apps.mail.views.client.DetailList import ListDetailCreateView
from apps.mail.views.client.DetailList import ListDetailUpdateView
from apps.mail.views.client.DetailList import ListDetailDeleteView
from apps.mail.views.client.DetailList import ListDetailUnSubscribeView


urlpatterns = patterns('',
                       url(r'^list-detail/(?P<pk>\d+)/$',
                           ListDetailView.as_view(),
                           name='list_detail_view'),

                       url(r'^create/(?P<list>\d+)/$',
                           ListDetailCreateView.as_view(),
                           name='list_detail_create_view'),

                       url(r'^update/(?P<pk>\d+)/$',
                           ListDetailUpdateView.as_view(),
                           name='list_detail_update_view'),

                       url(r'^delete/$',
                           ListDetailDeleteView.as_view(),
                           name='list_detail_delete_view'),

                       url(r'^unsubscribe/(?P<pk>\d+)/$',
                           ListDetailUnSubscribeView.as_view(),
                           name='list_detail_un_subscribe_view'),
                       )