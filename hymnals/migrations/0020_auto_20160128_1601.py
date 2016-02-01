# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0019_search_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='Authors',
            field=models.CharField(default=b'', max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='search',
            name='Name',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
