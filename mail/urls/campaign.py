from django.conf.urls import patterns, url

from mail.views.Campaign.send import SendMessage
from mail.views.Campaign.campaign import CampaignListView, \
    CampaignCreateView, CampaignUpdateView, CampaignDeleteView, \
    CampaignDetailListView

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
                       )