# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizations', '0004_auto_20160118_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='org',
            name='org_admins',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
