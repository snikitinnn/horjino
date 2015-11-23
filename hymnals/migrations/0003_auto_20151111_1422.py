# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0002_auto_20151109_1441'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['Name']},
        ),
    ]
