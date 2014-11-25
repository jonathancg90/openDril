from django.conf.urls import patterns, include, url

from apps.mail.views.dashboard import HomeTemplate
from apps.mail.views.dashboard import dashboardTemplate
from apps.mail.views.dashboard import LoginUserView
from apps.mail.views.dashboard import LogoutView
from apps.mail.views.dashboard import UnSubscribeView

urlpatterns = patterns('',
                       url(r'^$',
                           HomeTemplate.as_view(),
                           name='home_view'),

                       url(r'^dashboard/$',
                           dashboardTemplate.as_view(),
                           name='dashboard_view'),

                       url(r'^unsubscribe/(?P<pk>\d+)/$',
                           UnSubscribeView.as_view(),
                           name='un_subscribe_view'),

                       url(r'^login/$',
                           LoginUserView.as_view(),
                           name='login'),

                       url(r'^logout/$',
                           LogoutView.as_view(),
                           name='logout'),

                       url(r'^list/', include('apps.mail.urls.list')),
                       url(r'^list-detail/', include('apps.mail.urls.list_detail')),
                       url(r'^campaign/', include('apps.mail.urls.campaign')),
                       url(r'^template/', include('apps.mail.urls.template')),
                       url(r'^category/', include('apps.mail.urls.category')),
                       )