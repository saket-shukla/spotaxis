# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-27 12:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activities', '0003_auto_20161027_1103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['last_updated'], 'verbose_name': 'Notification', 'verbose_name_plural': 'Notifications'},
        ),
        migrations.AddField(
            model_name='notification',
            name='actor',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actor', to=settings.AUTH_USER_MODEL),
        ),
    ]