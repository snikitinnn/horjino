# -*- coding: UTF-8 -*-
from django.db import models
from django.utils import timezone

class User(models.Model):
    class Meta():
        db_table = 'auth_user'
    username = models.CharField(max_length=30)
    email = models.CharField(max_length = 254)
    password = models.CharField(default='qwerty', max_length = 128)
    is_superuser = models.BooleanField(default=0)
    def __unicode__(self):
        return self.username


class Post(models.Model):
    class Meta():
        db_table = 'blog_posts'

    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pubdate = models.DateField(default=timezone.now)
    category = models.CharField(max_length=30, default='private')
#    publiched_date = models.DateTimeField(blank=True, null=True)

    # def publish(self):
    #     self.pubdate = timezone.now()
    #     self.save()

    def __unicode__(self):
        return self.title
