# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-03 08:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0002_auto_20170803_0818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='product',
            new_name='project',
        ),
    ]
