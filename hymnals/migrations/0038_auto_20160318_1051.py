# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0037_auto_20160304_1253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ws',
            options={'ordering': ['-time']},
        ),
        migrations.AddField(
            model_name='ws',
            name='time',
            field=models.DateTimeField(default=0),
        ),
        migrations.AlterModelTable(
            name='ws',
            table='hymnals_ws',
        ),
    ]
