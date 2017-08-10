# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-06 06:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_service_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Material'),
        ),
    ]
