# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmInfo', '0006_remove_grows_crop_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='id',
        ),
        migrations.AlterField(
            model_name='crop',
            name='crop_name',
            field=models.CharField(max_length=200, serialize=False, primary_key=True),
        ),
    ]
