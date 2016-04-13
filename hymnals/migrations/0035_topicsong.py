# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0034_auto_20160302_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicSong',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('song', models.ForeignKey(to='hymnals.Song')),
                ('topic', models.ForeignKey(to='hymnals.Topic')),
            ],
        ),
    ]
