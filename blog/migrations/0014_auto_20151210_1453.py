# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_post_isnews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='isnews',
            field=models.BooleanField(),
        ),
    ]
