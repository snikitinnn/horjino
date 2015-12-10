# -*- coding: UTF-8 -*-
from django import forms
from blog.models import Post,User

class PostForms(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content',)
    title = forms.CharField(max_length=200)
    content = forms.Textarea()
    isnews = forms.CheckboxInput()

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password',)
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=128)
