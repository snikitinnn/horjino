# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0026_auto_20160201_0855'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='song',
            table='hymnals_song',
        ),
    ]
