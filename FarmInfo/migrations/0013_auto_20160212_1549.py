# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmInfo', '0012_auto_20160203_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farm_has_visit',
            name='farm_id',
        ),
        migrations.RemoveField(
            model_name='farm_has_visit',
            name='visit_id',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='crop_name',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='problem_type',
        ),
        migrations.RemoveField(
            model_name='visit_has_problem',
            name='problem_id',
        ),
        migrations.RemoveField(
            model_name='visit_has_problem',
            name='visit_id',
        ),
        migrations.DeleteModel(
            name='Farm_has_visit',
        ),
        migrations.DeleteModel(
            name='Problem',
        ),
        migrations.DeleteModel(
            name='Problem_type',
        ),
        migrations.DeleteModel(
            name='Visit',
        ),
        migrations.DeleteModel(
            name='Visit_has_problem',
        ),
    ]
