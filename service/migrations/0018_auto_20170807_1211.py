# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-07 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0017_auto_20170807_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='description',
            field=models.TextField(default='', verbose_name='Комплектация'),
        ),
    ]