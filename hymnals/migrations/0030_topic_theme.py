# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0029_song_accords'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='theme',
            field=models.ManyToManyField(to='hymnals.Song', through='hymnals.TopicvsSong'),
        ),
    ]
