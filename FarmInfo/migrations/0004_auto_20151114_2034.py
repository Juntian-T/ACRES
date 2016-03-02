# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmInfo', '0003_auto_20151113_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='lat',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=6),
        ),
        migrations.AlterField(
            model_name='farm',
            name='lon',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=6),
        ),
    ]
