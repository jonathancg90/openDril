# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    ROLE_ADMINISTRATOR = 1
    ROLE_DESIGN = 2
    ROLE_VIEWER = 3
    ROLE_AUTHOR = 4
    ROLE_NONE = None

    CHOICE_ROLES = (
        (ROLE_NONE, 'Seleccione'),
        (ROLE_AUTHOR, 'Autor'),
        (ROLE_VIEWER, 'Espectador'),
        (ROLE_DESIGN, 'Diseñador'),
        (ROLE_ADMINISTRATOR, 'Administrador')
    )
    user = models.OneToOneField(User,
                                related_name='user_profile_set',)

    role = models.SmallIntegerField(
        choices=CHOICE_ROLES,
        default=ROLE_ADMINISTRATOR
    )

    class Meta:
        app_label = 'mail'
