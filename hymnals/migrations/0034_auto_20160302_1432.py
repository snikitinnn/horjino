# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0033_auto_20160302_1303'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='topic',
            table='hymnals_topic',
        ),
        migrations.AlterModelTable(
            name='topicvssong',
            table='hymnals_topicvssong',
        ),
    ]
