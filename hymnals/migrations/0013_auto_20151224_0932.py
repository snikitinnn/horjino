# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnals', '0012_hymnal_chorus'),
    ]

    operations = [
        migrations.AddField(
            model_name='hymnal',
            name='icon',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='hymnal',
            name='Hymnal_Name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hymnal',
            name='Theme',
            field=models.CharField(max_length=65),
        ),
        migrations.AlterField(
            model_name='song',
            name='Authors',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='song',
            name='Authors_2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='song',
            name='Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='song',
            name='Name_Alt',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ws',
            name='Event',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ws',
            name='Note',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ws',
            name='Regents',
            field=models.CharField(max_length=100),
        ),
    ]
