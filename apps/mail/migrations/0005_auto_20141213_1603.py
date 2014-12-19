# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mail', '0004_auto_20141125_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=50)),
                ('logo', models.FileField(null=True, upload_to=b'business')),
                ('mandrill_api_key', models.CharField(max_length=150, verbose_name=b'Mandrill Key')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='campaign',
            name='business',
            field=models.ForeignKey(related_name=b'campaign_set', default=1, to='mail.Business'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='business',
            field=models.ForeignKey(related_name=b'category_set', default=1, to='mail.Business'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list',
            name='business',
            field=models.ForeignKey(related_name=b'list_set', default=1, to='mail.Business'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='template',
            name='business',
            field=models.ForeignKey(related_name=b'template_set', to='mail.Business', null=True),
            preserve_default=True,
        ),
    ]
