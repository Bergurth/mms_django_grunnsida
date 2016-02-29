# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_auto_20160118_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='org',
            name='description',
            field=models.CharField(max_length=520, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='org',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 18, 14, 21, 38, 636593, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='org',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 18, 14, 22, 0, 47260, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
