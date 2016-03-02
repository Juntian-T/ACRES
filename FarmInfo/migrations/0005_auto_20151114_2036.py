# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmInfo', '0004_auto_20151114_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='lat',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=6, blank=True),
        ),
        migrations.AlterField(
            model_name='farm',
            name='lon',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=6, blank=True),
        ),
    ]
