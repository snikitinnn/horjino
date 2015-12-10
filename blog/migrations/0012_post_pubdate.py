# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pubdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
