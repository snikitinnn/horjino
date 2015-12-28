# -*- coding: UTF-8 -*-
from django.db import models

class Chorus(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=120)
    def __unicode__(self):
        return self.name

class Hymnal(models.Model):
    Hymnal_Name = models.CharField(max_length=50)
    Theme = models.CharField(max_length=65)
    chorus = models.ForeignKey(Chorus, default=None)
    icon = models.CharField(default=None,max_length=50)
    class Meta:
        ordering = ['Hymnal_Name']
    def __unicode__(self):
        return self.Hymnal_Name

class Song(models.Model):
    Name = models.CharField(max_length=100)
    Name_Alt = models.CharField(max_length=100)
    hymnal = models.ForeignKey(Hymnal)
    Page_Score = models.IntegerField()
    Authors = models.CharField(max_length=50)
    Authors_2 = models.CharField(max_length=50)
    class Meta:
        ordering = ['Page_Score']
    def __unicode__(self):
        return self.Name

class WS(models.Model):
    Date = models.DateField()
    chorus = models.ForeignKey(Chorus)
    Supper = models.BooleanField()
    Regents = models.CharField(max_length=100)
    Event = models.CharField(max_length=100)
    Note = models.CharField(max_length=100)
    singing = models.ManyToManyField(Song, through='SongvsWS')
    class Meta:
        ordering = ['-Date']
    def __unicode__(self):
        return str(self.Date)

class SongvsWS(models.Model):
    song = models.ForeignKey(Song)
    ws = models.ForeignKey(WS, related_name='Date1')
    sequence = models.IntegerField()
    def page(self):
        return self.song.Page_Score
    def hymnal(self):
        return self.song.hymnal
    def date(self):
        return self.ws.Date
    def event(self):
        return self.ws.Event
    def chorus(self):
        return self.ws.chorus
    def __unicode__(self):
        return self.song.Name