# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-06 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmInfo', '0016_problem_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='img',
            field=models.ImageField(default=b'images/default.png', upload_to=b'images'),
        ),
    ]
