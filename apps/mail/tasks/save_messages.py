# -*- coding: utf-8 -*-
from celery.task import Task

from apps.mail.models.CampaignDetail import CampaignDetail
from apps.mail.models.ListDetail import ListDetail

class SaveMessagesMandrill(Task):

    name = 'save_messages_mandrill'

    def run(self, *args, **kwargs):
        campaign = kwargs.get('campaign')
        for campaign_detail_filter in campaign.campaign_filter_detail_set.all():
            if campaign_detail_filter.category is None:
                list_details = campaign_detail_filter.list.list_detail_set.filter(
                    status=ListDetail.STATUS_ACTIVE
                )
            else:
                list_details = campaign_detail_filter.list.list_detail_set.filter(
                    category=campaign_detail_filter.category,
                    status=ListDetail.STATUS_ACTIVE
                )

            for detail_list in list_details:
                campaign_detail = CampaignDetail()
                campaign_detail.campaign = campaign
                campaign_detail.name = detail_list.name
                campaign_detail.email = detail_list.email
                campaign_detail.content = campaign.template.content
                campaign_detail.email_sender = campaign_detail_filter.list.email
                campaign_detail.name_sender = campaign_detail_filter.list.sender
                campaign_detail.subject = campaign.subject
                campaign_detail.status = CampaignDetail.STATUS_WAIT
                campaign_detail.list_detail = detail_list.id
                campaign_detail.tag = '%s-%s' %(str(campaign.id),campaign.subject.replace(" ", "-"))
                campaign_detail.save()
