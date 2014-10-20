# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('subject', models.CharField(max_length=50)),
                ('status', models.SmallIntegerField(default=1, choices=[(0, b'inactivo'), (2, b'publish'), (1, b'activo')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('status', models.SmallIntegerField(default=1, choices=[(0, b'inactivo'), (1, b'activo')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=75)),
                ('status', models.SmallIntegerField(default=1, choices=[(0, b'inactivo'), (1, b'activo')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ListDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=45)),
                ('status', models.SmallIntegerField(default=1, choices=[(0, b'inactivo'), (1, b'activo')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(related_name=b'list_detail_set', verbose_name=b'categoria', to='mail.Category')),
                ('list', models.ForeignKey(related_name=b'list_detail_set', verbose_name=b'Lista', to='mail.List')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.SmallIntegerField(default=1, choices=[(1, b'Texto'), (2, b'Html')])),
                ('name', models.CharField(max_length=45)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='campaign',
            name='list',
            field=models.ManyToManyField(to='mail.List'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='template',
            field=models.ForeignKey(related_name=b'campaign_set', verbose_name=b'Plantilla', to='mail.Template'),
            preserve_default=True,
        ),
    ]
