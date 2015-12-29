# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_pubdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='isnews',
            field=models.BooleanField(default=False),
        ),
    ]
