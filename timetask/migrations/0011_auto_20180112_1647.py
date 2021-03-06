# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-12 08:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetask', '0010_plantastconfig_project_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=256, verbose_name='\u9879\u76ee\u7c7b\u578b')),
                ('name', models.CharField(max_length=256, verbose_name='\u9879\u76ee\u540d\u79f0')),
            ],
        ),
        migrations.AlterModelOptions(
            name='plantimeconfig',
            options={'verbose_name': '\u8ba1\u5212\u6267\u884c\u914d\u7f6e', 'verbose_name_plural': '\u8ba1\u5212\u6267\u884c\u914d\u7f6e'},
        ),
        migrations.AlterModelOptions(
            name='timetaskconfig',
            options={'verbose_name': '\u8ba1\u5212\u5b9a\u65f6\u4efb\u52a1', 'verbose_name_plural': '\u8ba1\u5212\u5b9a\u65f6\u4efb\u52a1'},
        ),
        migrations.AlterField(
            model_name='plantastconfig',
            name='plan_time',
            field=models.ForeignKey(max_length=256, on_delete=django.db.models.deletion.CASCADE, to='timetask.PlanTimeConfig', verbose_name='\u5177\u4f53\u6267\u884c\u65e5\u671f(h)'),
        ),
    ]
