from django.conf.urls import patterns, url

from apps.mail.views.client.Campaign.send import SendMessage
from apps.mail.views.client.Campaign.send import SendTestMessage
from apps.mail.views.client.Campaign.campaign import CampaignListView
from apps.mail.views.client.Campaign.campaign import CampaignDetailListView
from apps.mail.views.client.Campaign.campaign import CampaignCreateView
from apps.mail.views.client.Campaign.campaign import CampaignDeleteView
from apps.mail.views.client.Campaign.campaign import CampaignUpdateView
from apps.mail.views.client.Campaign.campaign import CampaignListDetailView
from apps.mail.views.client.Campaign.campaign import CampaignListDetailCreateView
from apps.mail.views.client.Campaign.campaign import CampaignListDetailDeleteView


urlpatterns = patterns('',
                       url(r'^list/$',
                           CampaignListView.as_view(),
                           name='campaign_list_view'),
                       url(r'^create/$',
                           CampaignCreateView.as_view(),
                           name='campaign_create_view'),
                       url(r'^update/(?P<pk>\d+)/$',
                           CampaignUpdateView.as_view(),
                           name='campaign_update_view'),
                       url(r'^delete/$',
                           CampaignDeleteView.as_view(),
                           name='campaign_delete_view'),


                       url(r'^detail-list/(?P<pk>\d+)/$',
                           CampaignDetailListView.as_view(),
                           name='campaign_detail_list_view'),

                       url(r'^send/(?P<campaign>\d+)/$',
                           SendMessage.as_view(),
                           name='send_messages_view'),

                       url(r'^send-test/(?P<campaign>\d+)/$',
                           SendTestMessage.as_view(),
                           name='send_test_message'),

                       url(r'^create-filter/$',
                           CampaignListDetailCreateView.as_view(),
                           name='campaign_filter_create_view'),

                       url(r'^delete-filter/$',
                           CampaignListDetailDeleteView.as_view(),
                           name='campaign_filter_delete_view'),

                       url(r'^get-filters/(?P<campaign>[^/]+)/$',
                           CampaignListDetailView.as_view(),
                           name='campaign_filter_view'),

                       )