# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20170829_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='business',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]