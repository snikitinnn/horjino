# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0013_auto_20151224_0932'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['Name']},
        ),
    ]
