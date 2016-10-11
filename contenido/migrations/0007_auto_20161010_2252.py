# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-11 03:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenido', '0006_auto_20161009_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='artista',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='audio',
            name='albums',
            field=models.ManyToManyField(blank=True, related_name='albums', to='contenido.Album'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
