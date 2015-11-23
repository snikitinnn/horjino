# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hymnal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Hymnal_Name', models.CharField(max_length=200)),
                ('Theme', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['Hymnal_Name'],
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=200)),
                ('Name_Alt', models.CharField(max_length=200)),
                ('Page_Score', models.IntegerField()),
                ('Authors', models.CharField(max_length=200)),
                ('Authors_2', models.CharField(max_length=200)),
                ('hymnal', models.ForeignKey(to='hymnals.Hymnal')),
            ],
        ),
        migrations.CreateModel(
            name='SongvsWS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Perform', models.IntegerField()),
                ('song', models.ForeignKey(to='hymnals.Song')),
            ],
        ),
        migrations.CreateModel(
            name='WS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Date', models.DateField()),
                ('chorus_id', models.IntegerField()),
                ('Supper', models.BooleanField()),
                ('Chorus_Name', models.CharField(max_length=200)),
                ('Regents', models.CharField(max_length=200)),
                ('Event', models.CharField(max_length=200)),
                ('Note', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['-Date'],
            },
        ),
        migrations.AddField(
            model_name='songvsws',
            name='ws',
            field=models.ForeignKey(related_name='Date1', to='hymnals.WS'),
        ),
    ]
