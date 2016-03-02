# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmInfo', '0007_auto_20151122_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='grows',
            name='crop_name',
            field=models.ForeignKey(to='FarmInfo.Crop', null=True),
        ),
    ]
