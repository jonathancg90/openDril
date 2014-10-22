# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0009_remove_campaign_multiple_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignFilterDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('campaign', models.ForeignKey(related_name=b'campaign_filter_detail_set', verbose_name=b'Campa\xc3\xb1a', to='mail.Campaign')),
                ('category', models.ForeignKey(related_name=b'campaign_filter_detail_set', verbose_name=b'Categoria', to='mail.Category')),
                ('list', models.ForeignKey(related_name=b'campaign_filter_detail_set', verbose_name=b'Lista', to='mail.List')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
