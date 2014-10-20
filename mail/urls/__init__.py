from django.conf.urls import patterns, include, url

from mail.views.dashboard import dashboardTemplate

urlpatterns = patterns('',
                       url(r'^$',
                           dashboardTemplate.as_view(),
                           name='dashboard_view'),
                       url(r'^list/', include('mail.urls.list')),
                       url(r'^list-detail/', include('mail.urls.list_detail')),
                       url(r'^campaign/', include('mail.urls.campaign')),
                       url(r'^template/', include('mail.urls.template')),
                       )