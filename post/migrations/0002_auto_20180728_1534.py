# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-28 07:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='post',
            table='posts',
        ),
    ]