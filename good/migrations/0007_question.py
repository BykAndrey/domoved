# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0006_auto_20170809_0910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('name', models.CharField(default='Name', max_length=40, verbose_name='ФИО')),
                ('email', models.EmailField(default='', max_length=254, verbose_name='Email')),
                ('telephone', models.CharField(default='+ 7(123) 456-78-91', max_length=13, verbose_name='Телефон')),
                ('boolVisible', models.BooleanField(default=False, verbose_name='Опубликовать')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]