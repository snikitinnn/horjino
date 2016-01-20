# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='isnews',
            field=models.BooleanField(default=False),
        ),
    ]
