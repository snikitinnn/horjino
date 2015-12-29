# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0006_auto_20151211_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='ws',
            name='singing',
            field=models.ManyToManyField(to='hymnals.Song', through='hymnals.SongvsWS'),
        ),
    ]
