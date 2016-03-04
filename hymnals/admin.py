# -*- coding: UTF-8 -*-
from django.contrib import admin
from django.forms import ModelForm
from hymnals.models import Chorus, Hymnal, Song, WS, SongvsWS, Topic, TopicSong


# class TopicvsSongInline(admin.TabularInline):
#     model = TopicvsSong
#     fk_name = 'topic'
#     extra = 0
#     list_display = ('song',)
#     fieldsets = [
#         (None,{'fields': ['song'],
#                'classes': ['collapse']}
#         ),
#     ]

class TopicSongInline(admin.TabularInline):
    model = TopicSong
    extra = 0
    list_display = ('song',)
    fieldsets = [
        (None,{'fields': ['song'],
               'classes': ['collapse']}
         ),
    ]

class TopicSong2Inline(admin.TabularInline):
    model = TopicSong
    extra = 0
    list_display = ('topic',)
    fieldsets = [
        (None,{'fields': ['topic'],
               'classes': ['collapse']}
         ),
    ]

class SongvsWSInline(admin.TabularInline):
    model = SongvsWS
    fk_name = 'ws'
    extra = 0
    list_display = ('sequence','song',)
    fieldsets = [
        (None,{'fields': ['sequence','song'],
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

class TopicAdmin(admin.ModelAdmin):
    inlines = [TopicSongInline,]
    list_display = ('name',)
    ordering = ['name']

class SongAdmin(admin.ModelAdmin):
#    form = SongAdminForm
    inlines = [TopicSong2Inline,]
    list_display = ('Name','Name_Alt','hymnal','Page_Score','Authors','Authors_2',)
    list_filter = ('Name',)

class WSAdmin(admin.ModelAdmin):
    inlines = [SongvsWSInline,]
    list_display = ('Date','Supper','chorus','Regents','Event','Note',)
    list_filter = ('chorus','Date',)

class HymnalAdmin(admin.ModelAdmin):
    inlines = [SongInline,]
    list_display = ('Hymnal_Name',)
    list_filter = ('Hymnal_Name',)

class SongvsWSAdmin(admin.ModelAdmin):
    list_display = ('ws','song','sequence',)
    list_filter = ('ws__Date','song__hymnal__Hymnal_Name','song',)

class TopicSongAdmin(admin.ModelAdmin):
    list_display = ('topic','song')
    list_filter = ('topic','song')

admin.site.register(Chorus)
admin.site.register(Song, SongAdmin)
admin.site.register(Hymnal, HymnalAdmin)
admin.site.register(WS, WSAdmin)
admin.site.register(SongvsWS, SongvsWSAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(TopicSong, TopicSongAdmin)