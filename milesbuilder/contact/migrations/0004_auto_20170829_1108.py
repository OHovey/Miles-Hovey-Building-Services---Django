# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 11:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20170829_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 29, 11, 8, 8, 372521, tzinfo=utc)),
        ),
    ]