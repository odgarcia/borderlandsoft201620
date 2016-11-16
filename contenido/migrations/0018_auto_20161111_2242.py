# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-12 03:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenido', '0017_auto_20161111_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='ind_estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterUniqueTogether(
            name='ratings',
            unique_together=set([('autor', 'audio')]),
        ),
    ]
