# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-08 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetask', '0005_auto_20180108_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantastconfig',
            name='name',
            field=models.CharField(max_length=256, verbose_name='\u4efb\u52a1\u540d\u79f0'),
        ),
    ]
