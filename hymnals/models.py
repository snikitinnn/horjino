# -*- coding: UTF-8 -*-
from django.db import models
import datetime
import time

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
    active = models.BooleanField(default=False)
    color = models.CharField(max_length=20, default=None)
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
    accords = models.IntegerField(default=0)
    over = models.IntegerField(default=0)
    class Meta:
        db_table = 'hymnals_song'
        ordering = ['Name']#ordering = ['Page_Score']
    def __unicode__(self):
        return self.Name

class WS(models.Model):
    Date = models.DateField()
    time = models.DateTimeField(default=0)
    chorus = models.ForeignKey(Chorus)
    Supper = models.BooleanField()
    Regents = models.CharField(max_length=100)
    Event = models.CharField(max_length=100)
    Note = models.CharField(max_length=100)
    singing = models.ManyToManyField(Song, through='SongvsWS')
    class Meta:
        ordering = ['-time']
        db_table = 'hymnals_ws'
    def __unicode__(self):
        return str(self.Date)


class SongvsWS(models.Model):
    song = models.ForeignKey(Song)
    ws = models.ForeignKey(WS) #)related_name='Date1')
    sequence = models.IntegerField()
    class Mets:
        db_table = 'hymnals_songvsws'
    def page(self):
        return self.song.Page_Score
    def hymnal(self):
        return self.song.hymnal
    def date(self):
        return self.ws.Date
    def time(self):
        return self.ws.time
    def event(self):
        return self.ws.Event
    def chorus(self):
        return self.ws.chorus
    def accords(self):
        return self.song.accords
    def __unicode__(self):
        return self.song.Name

class Topic(models.Model):
    class Meta:
        db_table = 'hymnals_topic'
        ordering = ['name']
    name = models.CharField(max_length=40)
    theme = models.ManyToManyField(Song, through='TopicSong')
    def __unicode__(self):
        return self.name

class TopicSong(models.Model):
    topic = models.ForeignKey(Topic)
    song = models.ForeignKey(Song)
    def page(self):
        return self.song.Page_Score
    def hymnal(self):
        return self.song.hymnal
    def chorus(self):
        return self.song.hymnal.chorus
    def accords(self):
        return self.song.accords
    def __unicode__(self):
        return self.song.Name


# class TopicvsSong(models.Model):
#     class Meta:
#         db_table = 'hymnals_topicvssong'
#     topic = models.ForeignKey(Topic)
#     song = models.ForeignKey(Song)
#     def page(self):
#         return self.song.Page_Score
#     def hymnal(self):
#         return self.song.hymnal
#     def chorus(self):
#         return self.song.hymnal.chorus
#     def accords(self):
#         return self.song.accords
#     def topic(self):
#         return self.topic.name
#     def __unicode__(self):
#         return self.song.Name


class Search(models.Model):
    Name = models.CharField(max_length=100)