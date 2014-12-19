# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mail', '0005_auto_20141213_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.SmallIntegerField(default=1, choices=[(None, b'Seleccione'), (4, b'Autor'), (3, b'Espectador'), (2, b'Dise\xc3\xb1ador'), (1, b'Administrador')])),
                ('user', models.OneToOneField(related_name=b'user_profile_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
