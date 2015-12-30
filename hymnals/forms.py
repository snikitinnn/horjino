# -*- coding: UTF-8 -*-
from django import forms

from models import Chorus


class ChorusForm(forms.ModelForm):

    class Meta:
        model = Chorus
        fields = ('name',)
    name = forms.CharField(max_length=200)
    content = forms.Textarea()
    isnews = forms.CheckboxInput()
