# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-18 05:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0018_auto_20161023_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='talkgroup',
            name='comments',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
