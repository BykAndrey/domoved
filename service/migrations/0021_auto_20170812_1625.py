# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0020_auto_20170812_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(default=' ', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.CharField(default=' ', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.CharField(default=' ', max_length=200, unique=True),
        ),
    ]