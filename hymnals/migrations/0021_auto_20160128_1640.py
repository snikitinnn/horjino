# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0020_auto_20160128_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='Authors',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
