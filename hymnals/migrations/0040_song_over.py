# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0039_auto_20160325_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='over',
            field=models.IntegerField(default=0),
        ),
    ]
