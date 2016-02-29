# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0005_org_org_admins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='org_admins',
            field=models.ManyToManyField(related_name='orgs_adm', to=settings.AUTH_USER_MODEL),
        ),
    ]
