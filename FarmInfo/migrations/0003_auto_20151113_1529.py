# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmInfo', '0002_auto_20151113_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='children',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='pet',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='spouse',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='farm',
            name='lat',
            field=models.DecimalField(max_digits=9, decimal_places=6, blank=True),
        ),
        migrations.AlterField(
            model_name='farm',
            name='lon',
            field=models.DecimalField(max_digits=9, decimal_places=6, blank=True),
        ),
        migrations.AlterField(
            model_name='farm',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='farm',
            name='office_num',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='farm',
            name='web',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
