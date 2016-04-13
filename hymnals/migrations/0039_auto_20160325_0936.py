# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0038_auto_20160318_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='hymnal',
            name='color',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='songvsws',
            name='ws',
            field=models.ForeignKey(to='hymnals.WS'),
        ),
    ]
