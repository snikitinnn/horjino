# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0016_search'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search',
            old_name='title',
            new_name='Name',
        ),
    ]
