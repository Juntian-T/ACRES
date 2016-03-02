# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('spouse', models.CharField(max_length=200)),
                ('children', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('pet', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crop_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('farm_name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('office_num', models.CharField(max_length=200)),
                ('fax', models.CharField(max_length=200)),
                ('web', models.CharField(max_length=200)),
                ('notes', models.TextField()),
                ('lon', models.DecimalField(max_digits=9, decimal_places=6)),
                ('lat', models.DecimalField(max_digits=9, decimal_places=6)),
            ],
        ),
        migrations.CreateModel(
            name='Grows',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crop_id', models.ForeignKey(to='FarmInfo.Crop')),
                ('farm_id', models.ForeignKey(to='FarmInfo.Farm')),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.ForeignKey(to='FarmInfo.Client')),
                ('farm_id', models.ForeignKey(to='FarmInfo.Farm')),
            ],
        ),
    ]
