# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-27 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0009_auto_20160908_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculum',
            name='filecontent',
            field=models.TextField(blank=True, default=b'', null=True),
        ),
    ]