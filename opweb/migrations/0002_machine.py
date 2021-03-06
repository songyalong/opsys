# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physical_host_name', models.CharField(max_length=200, null=True, verbose_name=b'\xe7\x89\xa9\xe7\x90\x86\xe6\x9c\xba\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d')),
                ('physical_host_IP', models.GenericIPAddressField(null=True, verbose_name=b'\xe7\x89\xa9\xe7\x90\x86\xe6\x9c\xbaIP')),
                ('machine_hostname', models.CharField(max_length=200, null=True, verbose_name=b'\xe8\x99\x9a\xe6\x8b\x9f\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d')),
                ('cpu_count', models.SmallIntegerField(null=True, verbose_name=b'CPU\xe6\xa0\xb8\xe6\x95\xb0')),
                ('memory_size', models.SmallIntegerField(null=True, verbose_name=b'\xe5\x86\x85\xe5\xad\x98\xe5\xa4\xa7\xe5\xb0\x8f')),
                ('disk_size', models.SmallIntegerField(null=True, verbose_name=b'\xe7\xa3\x81\xe7\x9b\x98\xe5\xa4\xa7\xe5\xb0\x8f')),
                ('os', models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe7\xb3\xbb\xe7\xbb\x9f')),
                ('machine_IP', models.GenericIPAddressField(null=True, verbose_name=b'\xe8\x99\x9a\xe6\x8b\x9f\xe4\xb8\xbb\xe6\x9c\xbaIP')),
                ('is_running', models.SmallIntegerField(null=True, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
                ('allocate_time', models.CharField(max_length=100, null=True, verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe9\x83\xa8\xe9\x97\xa8')),
                ('machine_password', models.CharField(max_length=200, null=True, verbose_name=b'\xe6\x9c\xba\xe5\x99\xa8\xe5\xaf\x86\xe7\xa0\x81')),
            ],
        ),
    ]
