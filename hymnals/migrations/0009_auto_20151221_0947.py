# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0008_auto_20151219_1003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songvsws',
            old_name='Perform',
            new_name='sequence',
        ),
    ]
