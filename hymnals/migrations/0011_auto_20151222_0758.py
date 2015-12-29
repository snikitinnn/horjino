# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0010_auto_20151222_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ws',
            name='chorus',
            field=models.ForeignKey(to='hymnals.Chorus'),
        ),
    ]
