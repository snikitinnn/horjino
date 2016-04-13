# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0028_topic_topicvssong'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='accords',
            field=models.IntegerField(default=0),
        ),
    ]
