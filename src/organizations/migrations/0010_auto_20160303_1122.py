# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizations', '0009_auto_20160205_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=228)),
                ('year', models.DateField()),
                ('associated_teacher', models.ForeignKey(related_name='associated_teacher', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent_org', models.ForeignKey(related_name='parent_org', to='organizations.Org')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='ss_number',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(related_name='students', to='organizations.Student'),
        ),
    ]
