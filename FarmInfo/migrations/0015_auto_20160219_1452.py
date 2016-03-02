# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmInfo', '0014_auto_20160212_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problem_specifics',
            old_name='type_id',
            new_name='type_name',
        ),
    ]
