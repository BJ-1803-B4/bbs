# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-28 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
    ]
