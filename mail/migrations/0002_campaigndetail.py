# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=45)),
                ('mandrill_id', models.CharField(max_length=100)),
                ('status', models.SmallIntegerField(default=1, choices=[(0, b'rechazado'), (2, b'abierto'), (1, b'enviado')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('campaign', models.ForeignKey(related_name=b'campaign_detail_set', verbose_name=b'Campa\xc3\xb1a', to='mail.Campaign')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
