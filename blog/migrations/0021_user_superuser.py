# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20160114_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='superuser',
            field=models.BigIntegerField(default=0),
        ),
    ]
