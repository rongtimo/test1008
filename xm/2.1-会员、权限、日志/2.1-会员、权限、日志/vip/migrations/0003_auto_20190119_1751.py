# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-19 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vip', '0002_permission_desc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vip',
            options={'ordering': ['level']},
        ),
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(max_length=16, unique=True, verbose_name='权限名称'),
        ),
        migrations.AlterField(
            model_name='vip',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='会员等级对应的名称'),
        ),
    ]
