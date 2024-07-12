# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-27 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0006_notification_actor_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='template',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='activities.NotificationTemplate'),
        ),
    ]