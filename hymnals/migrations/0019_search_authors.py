# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0018_search_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='Authors',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
