# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0019_auto_20170812_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, default=' ', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.CharField(blank=True, default=' ', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.CharField(blank=True, default=' ', max_length=200, unique=True),
        ),
    ]
