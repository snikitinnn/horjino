# -*- coding: UTF-8 -*-
from django import forms
from blog.models import Post

class PostForms(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'pubdate',)
    title = forms.CharField(max_length=200)
    content = forms.Textarea()
    pubdate = forms.DateField()