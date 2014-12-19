from django.conf.urls import patterns, url

from apps.mail.views.client.Template import TemplateView
from apps.mail.views.client.Template import TemplateCreateView
from apps.mail.views.client.Template import TemplateUpdateView
from apps.mail.views.client.Template import TemplateDeleteView


urlpatterns = patterns('',
                       url(r'^$',
                           TemplateView.as_view(),
                           name='template_list_view'),

                       url(r'^create/$',
                           TemplateCreateView.as_view(),
                           name='template_create_view'),

                       url(r'^update/(?P<pk>\d+)/$',
                           TemplateUpdateView.as_view(),
                           name='template_update_view'),

                       url(r'^delete/$',
                           TemplateDeleteView.as_view(),
                           name='template_delete_view'),
                       )