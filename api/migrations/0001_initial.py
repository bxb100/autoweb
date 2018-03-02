# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-27 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='\u63a5\u53e3\u540d\u79f0')),
                ('is_run', models.BooleanField(default=False, verbose_name='\u72b6\u6001')),
                ('pre_data_file', models.FileField(blank=True, null=True, upload_to='uploads/script/', verbose_name='\u6570\u636e\u6587\u4ef6')),
                ('script_path', models.FileField(blank=True, null=True, upload_to='uploads/script/', verbose_name='\u7528\u4f8b\u6587\u4ef6')),
                ('schedule', models.CharField(blank=True, max_length=256, null=True, verbose_name='\u8fdb\u5ea6')),
                ('result', models.FileField(upload_to='uploads/script/', verbose_name='\u6267\u884c\u7ed3\u679c')),
                ('creater', models.CharField(blank=True, max_length=256, null=True, verbose_name='\u521b\u5efa\u4eba')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'API\u7528\u4f8b\u7ba1\u7406',
                'verbose_name_plural': 'API\u7528\u4f8b\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='ProjectConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='\u63a5\u53e3\u9879\u76ee')),
            ],
            options={
                'verbose_name': '\u9879\u76ee\u914d\u7f6e',
                'verbose_name_plural': '\u9879\u76ee\u914d\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='VersionConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='\u7248\u672c')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ProjectConfig', verbose_name='\u6240\u5c5e\u9879\u76ee')),
            ],
            options={
                'verbose_name': '\u7248\u672c\u914d\u7f6e',
                'verbose_name_plural': '\u7248\u672c\u914d\u7f6e',
            },
        ),
        migrations.AddField(
            model_name='apitest',
            name='class_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.VersionConfig', verbose_name='\u7248\u672c'),
        ),
        migrations.AddField(
            model_name='apitest',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ProjectConfig', verbose_name='\u9879\u76ee'),
        ),
    ]