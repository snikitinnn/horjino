# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0024_auto_20160201_0803'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='search',
            table='hymnals_song',
        ),
    ]
