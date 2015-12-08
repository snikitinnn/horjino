# -*- coding: UTF-8 -*-
from django.db import models
from django.utils import timezone

class Post(models.Model):
    class Meta():
        db_table = 'blog_posts'

    user = models.ForeignKey('auth.user', default=1)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pubdate = models.DateTimeField(default=timezone.now)
#    publiched_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title


# Create your models here.
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __unicode__(self):              # __unicode__ on Python 2
#         return self.question_text
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __unicode__(self):              # __unicode__ on Python 2
#         return self.choice_text