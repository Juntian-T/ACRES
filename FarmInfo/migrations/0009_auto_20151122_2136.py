# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmInfo', '0008_grows_crop_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farm',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='farm',
            name='lon',
        ),
    ]
