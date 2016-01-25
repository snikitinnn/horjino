# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20160121_1139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='superuser',
            new_name='is_superuser',
        ),
    ]
