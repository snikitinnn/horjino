# -*- coding: UTF-8 -*-
from django.contrib import admin
from django.forms import ModelForm
from hymnals.models import Chorus, Hymnal, Song, WS, SongvsWS

class SongvsWSInline(admin.TabularInline):
    model = SongvsWS
    fk_name = 'ws'
    extra = 0
    list_display = ('Perform','song',)
    fieldsets = [
        (None,{'fields': ['Perform','song'],
               'classes': ['collapse']}
        ),
    ]

class SongInline(admin.TabularInline):
    model = Song
    extra = 0
    list_display = ('Name','Name_Alt','Page_Score','Authors','Authors_2',)
    fieldsets = [
        (None,{'fields': ['Authors','Authors_2','Page_Score','Name','Name_Alt'],
               'classes': ['collapse']}
        ),
    ]

#################################

def get_my_choices():
    choices_list = (
                ('accepted', 'Accepted'),
                ('denied', 'Denied'),
            )
    return choices_list

# class SongAdminForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(SongAdminForm, self).__init__(*args, **kwargs)
#         self.fields['my_choice_field'] = forms.ChoiceField(choices=get_my_choices())
#     class Meta:
#         model = Song
#
#     def clean_name(self):
#         # do something that validates your data
#         return self.cleaned_data["name"]

class SongAdmin(admin.ModelAdmin):
#    form = SongAdminForm
    list_display = ('Name','Name_Alt','hymnal','Page_Score','Authors','Authors_2',)
    list_filter = ('Name',)

class WSAdmin(admin.ModelAdmin):
    inlines = [SongvsWSInline,]
    list_display = ('Date','Supper','Chorus_Name','Regents','Event','Note',)
    list_filter = ('Chorus_Name','Date',)

class HymnalAdmin(admin.ModelAdmin):
    inlines = [SongInline,]
    list_display = ('Hymnal_Name',)
    list_filter = ('Hymnal_Name',)

class SongvsWSAdmin(admin.ModelAdmin):
    list_display = ('ws','song','Perform')
    list_filter = ('ws__Date','song__hymnal__Hymnal_Name','song',)

admin.site.register(Chorus)
admin.site.register(Song, SongAdmin)
admin.site.register(Hymnal, HymnalAdmin)
admin.site.register(WS, WSAdmin)
admin.site.register(SongvsWS, SongvsWSAdmin)