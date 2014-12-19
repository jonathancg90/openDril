from django.conf.urls import patterns, url

from apps.mail.views.client.Category import CategoryTemplateView
from apps.mail.views.client.Category import CategoryCreateView
from apps.mail.views.client.Category import CategoryUpdateView
from apps.mail.views.client.Category import CategoryDeleteView


urlpatterns = patterns('',
                       url(r'^$',
                           CategoryTemplateView.as_view(),
                           name='category_list_view'),
                       url(r'^create/$',
                           CategoryCreateView.as_view(),
                           name='category_create_view'),
                       url(r'^update/(?P<pk>\d+)/$',
                           CategoryUpdateView.as_view(),
                           name='category_update_view'),
                       url(r'^delete/$',
                           CategoryDeleteView.as_view(),
                           name='category_delete_view'),
                       )