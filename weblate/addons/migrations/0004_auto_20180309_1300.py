# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-09 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addons', '0003_install_addons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event',
            field=models.IntegerField(choices=[(1, 'post push'), (2, 'post update'), (3, 'pre commit'), (4, 'post commit'), (5, 'post add'), (6, 'unit post create'), (7, 'store post load')]),
        ),
    ]
