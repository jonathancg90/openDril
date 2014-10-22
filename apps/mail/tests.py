# -*- coding: utf-8 -*-

from django.test import TestCase
from apps.mail.tasks.send_messages import SendMessagesMandrill

from apps.mail.models.Campaign import Campaign
from apps.mail.models.List import List
from apps.mail.models.ListDetail import ListDetail
from apps.mail.models.Template import Template
from apps.mail.models.CampaignDetail import CampaignDetail


class FacebookTaskTest(TestCase):

    def setUp(self):
        self.insert_data_test()
        self.send_message_mandrill = SendMessagesMandrill()

    def insert_data_test(self):
        list = List()
        list.name = 'lista de prueba'
        list.email = 'sistemas3@nexonet.net'
        list.sender = 'sistemas3'
        list.save()

        list_detail = ListDetail()
        list_detail.list = list
        list_detail.email = 'jonathancg90@gmail.com'
        list_detail.name = 'Jonathan'
        list_detail.save()

        template = Template()
        template.type = Template.TYPE_HTML
        template.name = 'template de prueba'
        template.content = '<h1>Hello World</h1>'
        template.save()

        campaign = Campaign()
        campaign.name = 'campaña de prueba'
        campaign.subject = 'esta es una prueba2333'
        campaign.template = template
        campaign.status = Campaign.STATUS_PROGRESS
        campaign.save()

        campaign.list.add(list)

        campaign_detail = CampaignDetail()
        campaign_detail.campaign = campaign
        campaign_detail.name = list_detail.name
        campaign_detail.email = list_detail.email
        campaign_detail.email_sender = list.email
        campaign_detail.name_sender = list.sender
        campaign_detail.subject = campaign.subject
        campaign_detail.tag = '%s-%s' %(str(campaign.id),campaign.subject.replace(" ", "-"))
        campaign_detail.content = template.content
        campaign_detail.status = CampaignDetail.STATUS_WAIT
        campaign_detail.save()


    def test_method_test_real(self):
        self.send_message_mandrill.run()
