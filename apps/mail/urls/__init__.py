from django.conf.urls import patterns, include, url

from apps.mail.views.dashboard import dashboardTemplate

urlpatterns = patterns('',
                       url(r'^$',
                           dashboardTemplate.as_view(),
                           name='dashboard_view'),
                       url(r'^list/', include('apps.mail.urls.list')),
                       url(r'^list-detail/', include('apps.mail.urls.list_detail')),
                       url(r'^campaign/', include('apps.mail.urls.campaign')),
                       url(r'^template/', include('apps.mail.urls.template')),
                       )