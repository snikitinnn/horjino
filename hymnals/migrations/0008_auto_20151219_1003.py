# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0007_ws_singing'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['Page_Score']},
        ),
    ]
