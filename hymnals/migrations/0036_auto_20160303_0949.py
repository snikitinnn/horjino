# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0035_topicsong'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topicvssong',
            name='song',
        ),
        migrations.AddField(
            model_name='topic',
            name='theme',
            field=models.ManyToManyField(to='hymnals.Song', through='hymnals.TopicSong'),
        ),
        migrations.DeleteModel(
            name='TopicvsSong',
        ),
    ]
