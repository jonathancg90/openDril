from django.conf.urls import patterns, url
from mail.views.DetailList import ListDetailView
from mail.views.DetailList import ListDetailCreateView
from mail.views.DetailList import ListDetailUpdateView
from mail.views.DetailList import ListDetailDeleteView

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
                       )