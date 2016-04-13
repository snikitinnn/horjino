# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0031_auto_20160301_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topicvssong',
            old_name='topic',
            new_name='topic2',
        ),
        migrations.AlterModelTable(
            name='topicvssong',
            table=None,
        ),
    ]
