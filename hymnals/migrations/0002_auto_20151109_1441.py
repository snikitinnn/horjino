# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0001_initial'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='songvsws',
            order_with_respect_to='song',
        ),
    ]
