# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-10 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lang', '0004_auto_20161222_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='pluralequation',
            field=models.CharField(blank=True, max_length=400, verbose_name='Plural equation'),
        ),
    ]
