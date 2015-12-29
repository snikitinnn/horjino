# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0009_auto_20151221_0947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ws',
            old_name='chorus_id',
            new_name='chorus',
        ),
        migrations.RemoveField(
            model_name='ws',
            name='Chorus_Name',
        ),
    ]
