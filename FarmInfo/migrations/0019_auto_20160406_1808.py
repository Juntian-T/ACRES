# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-06 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmInfo', '0018_auto_20160406_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='img',
            field=models.ImageField(default=b'images/default.png', upload_to=b'images'),
        ),
    ]
