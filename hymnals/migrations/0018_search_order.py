# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0017_auto_20160127_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='order',
            field=models.CharField(default=b'n', max_length=10),
        ),
    ]
