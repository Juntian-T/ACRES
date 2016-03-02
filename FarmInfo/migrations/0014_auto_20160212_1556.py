# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('FarmInfo', '0013_auto_20160212_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farm_has_visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('farm_id', models.ForeignKey(to='FarmInfo.Farm')),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notes', models.TextField(blank=True)),
                ('crop_name', models.ForeignKey(to='FarmInfo.Crop')),
                ('farm_id', models.ForeignKey(to='FarmInfo.Farm')),
            ],
        ),
        migrations.CreateModel(
            name='Problem_has_specifics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('problem_id', models.ForeignKey(to='FarmInfo.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='Problem_specifics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Problem_type',
            fields=[
                ('type_name', models.CharField(max_length=200, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visit_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Visit_has_problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('problem_id', models.ForeignKey(to='FarmInfo.Problem')),
                ('visit_id', models.ForeignKey(to='FarmInfo.Visit')),
            ],
        ),
        migrations.AddField(
            model_name='problem_specifics',
            name='type_id',
            field=models.ForeignKey(to='FarmInfo.Problem_type'),
        ),
        migrations.AddField(
            model_name='problem_has_specifics',
            name='specific_id',
            field=models.ForeignKey(to='FarmInfo.Problem_specifics'),
        ),
        migrations.AddField(
            model_name='farm_has_visit',
            name='visit_id',
            field=models.ForeignKey(to='FarmInfo.Visit'),
        ),
    ]
