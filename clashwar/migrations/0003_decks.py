# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clashwar', '0002_popularcards'),
    ]

    operations = [
        migrations.CreateModel(
            name='Decks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('place', models.CharField(max_length=30)),
                ('img', models.CharField(max_length=30)),
            ],
        ),
    ]
