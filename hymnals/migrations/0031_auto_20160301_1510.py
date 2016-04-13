# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0030_topic_theme'),
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
