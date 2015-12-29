# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0014_auto_20151228_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='hymnal',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
