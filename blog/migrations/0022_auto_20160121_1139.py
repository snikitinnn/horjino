# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_user_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='superuser',
            field=models.BooleanField(default=0),
        ),
    ]
