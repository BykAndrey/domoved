# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0018_auto_20170807_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='keywords',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='keywords',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='keywords',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
    ]