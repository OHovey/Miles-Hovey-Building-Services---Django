# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 11:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20170829_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]