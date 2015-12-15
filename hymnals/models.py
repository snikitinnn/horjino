# -*- coding: UTF-8 -*-
from django.db import models

class Chorus(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=120)
    def __unicode__(self):
        return self.name

class Hymnal(models.Model):
    Hymnal_Name = models.CharField(max_length=200)
    Theme = models.CharField(max_length=200)
    class Meta:
        ordering = ['Hymnal_Name']
    def __unicode__(self):
        return self.Hymnal_Name

class Song(models.Model):
    Name = models.CharField(max_length=200)
    Name_Alt = models.CharField(max_length=200)
    hymnal = models.ForeignKey(Hymnal)
    Page_Score = models.IntegerField()
    Authors = models.CharField(max_length=200)
    Authors_2 = models.CharField(max_length=200)
    class Meta:
        ordering = ['Name']
    def __unicode__(self):
        return self.Name

class WS(models.Model):
    Date = models.DateField()
    chorus_id = models.IntegerField()
    Supper = models.BooleanField()
    Chorus_Name = models.CharField(max_length=200)
    Regents = models.CharField(max_length=200)
    Event = models.CharField(max_length=200)
    Note = models.CharField(max_length=200)
#    singing = models.ManyToManyField(Song, through='SongvsWS')
    class Meta:
        ordering = ['-Date']
    def __unicode__(self):
        return str(self.Date)

class SongMan(models.Manager):
    def get_queryset(self):
        return SongMan(self)
#    class Meta:
#        ordering = ['song']

class SongvsWS(models.Model):
    song = models.ForeignKey(Song)
    ws = models.ForeignKey(WS, related_name='Date1')
    Perform = models.IntegerField()

#    objects = models.Manager()
#    song_name = SongMan()
#    class Meta:
#        ordering = ['song']
    def __unicode__(self):
        return str(self.Perform)
