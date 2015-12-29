# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0005_choir'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choir',
            new_name='Chorus',
        ),
    ]
