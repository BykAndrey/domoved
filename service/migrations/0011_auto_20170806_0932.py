# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-06 09:32
from __future__ import unicode_literals

from django.db import migrations, models
import good.models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_auto_20170806_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=good.models.make_upload_path, verbose_name='Картинка'),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=good.models.make_upload_path, verbose_name='Картинка'),
        ),
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=good.models.make_upload_path, verbose_name='Картинка'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]