# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0022_auto_20160129_1343'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='search',
            table='hymnals_song',
        ),
    ]
