from django.conf.urls import patterns, include, url

from apps.mail.views.dashboard import HomeTemplate, dashboardTemplate, LoginUserView, LogoutView

urlpatterns = patterns('',
                       url(r'^$',
                           HomeTemplate.as_view(),
                           name='home_view'),

                       url(r'^dashboard/$',
                           dashboardTemplate.as_view(),
                           name='dashboard_view'),

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