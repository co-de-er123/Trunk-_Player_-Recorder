# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-25 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        #('pinax_stripe', '0007_auto_20170108_1202'),
        ('radio', '0037_add_default_plan_html'),
    ]

    operations = [
        migrations.CreateModel(
            name='StripePlanMatrix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('radio_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.Plan')),
                #('stripe_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Plan')),
            ],
        ),
    ]

