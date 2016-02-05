# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsletter', '0007_org_org_exec'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('ss_number', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=228)),
                ('date_of_birth', models.DateTimeField(null=True, blank=True)),
                ('sex', models.IntegerField(null=True, blank=True)),
                ('user', models.ForeignKey(related_name='student_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
