# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 22:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20171129_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 29, 22, 18, 15, 708192, tzinfo=utc)),
        ),
    ]
