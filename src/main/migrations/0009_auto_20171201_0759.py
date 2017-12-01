# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-01 00:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20171201_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 1, 0, 59, 43, 204240, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='order_history',
            field=models.ManyToManyField(blank='true', null='true', to='main.Order'),
        ),
    ]