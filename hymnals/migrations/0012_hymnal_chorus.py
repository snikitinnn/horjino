# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0011_auto_20151222_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='hymnal',
            name='chorus',
            field=models.ForeignKey(default=None, to='hymnals.Chorus'),
        ),
    ]
