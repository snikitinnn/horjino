# -*- coding: UTF-8 -*-
from django.db import models
from django.utils import timezone

class User(models.Model):
    class Meta():
        db_table = 'auth_users'
    username = models.CharField(max_length=30)
    email = models.CharField(max_length = 254)
    password = models.CharField(max_length = 128)

class Post(models.Model):
    class Meta():
        db_table = 'blog_posts'

#    user = models.ForeignKey(User, default=1)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pubdate = models.DateField(default=timezone.now)
    isnews = models.BooleanField()
#    publiched_date = models.DateTimeField(blank=True, null=True)

    # def publish(self):
    #     self.pubdate = timezone.now()
    #     self.save()

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