# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0021_auto_20160128_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='Authors',
        ),
        migrations.RemoveField(
            model_name='search',
            name='order',
        ),
        migrations.AlterField(
            model_name='search',
            name='Name',
            field=models.CharField(max_length=100),
        ),
    ]
