# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0032_auto_20160302_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='theme',
        ),
        migrations.RemoveField(
            model_name='topicvssong',
            name='topic2',
        ),
        migrations.AlterModelTable(
            name='topic',
            table=None,
        ),
    ]
