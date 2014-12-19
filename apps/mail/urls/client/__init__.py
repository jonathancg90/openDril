from django.conf.urls import patterns, include, url

from apps.mail.views.client.dashboard import DashboardTemplate
from apps.mail.views.client.dashboard import UnSubscribeView

urlpatterns = patterns('',
                       url(r'^dashboard/$',
                           DashboardTemplate.as_view(),
                           name='dashboard_view'),

                       url(r'^unsubscribe/(?P<pk>\d+)/$',
                           UnSubscribeView.as_view(),
                           name='un_subscribe_view'),

                       url(r'^list/', include('apps.mail.urls.client.list')),
                       url(r'^list-detail/', include('apps.mail.urls.client.list_detail')),
                       url(r'^campaign/', include('apps.mail.urls.client.campaign')),
                       url(r'^template/', include('apps.mail.urls.client.template')),
                       url(r'^category/', include('apps.mail.urls.client.category')),
                       )