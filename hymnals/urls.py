# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url

from hymnals import views

urlpatterns = patterns('',
    url(r'^choir/(?P<chorus_id>\d+)/$', views.choir, name='choir'),
    url(r'^(?P<hymnal_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<hymnal_id>\d+)/(?P<song_id>\d+)/$', views.results, name='results'),
    url(r'^song/(?P<song_id>\d+)/$', views.results_song, name='song'),
    url(r'^song/lyrics/(?P<song_id>\d+)/$', views.lyrics, name='lyrics'),
    url(r'^alphabet/$', views.alphabet, name='alphabet'),
    url(r'^alphabet/chorus/(?P<chorus_id>\d+)/$', views.alphabet_chorus, name='alphabet_chorus'),                       
    url(r'^ws/$', views.ws, name='ws'),
    url(r'^ws/last/$', views.ws_last, name='ws_last'),
    url(r'^ws/chorus/(?P<chorus_id>\d+)/$', views.ws_chorus, name='ws_chorus'),
    url(r'^ws/(?P<ws_id>\d+)/$', views.detail_ws, name='detail_ws'),
    url(r'^ws/(?P<ws_id>\d+)/(?P<song_id>\d+)/$', views.results_ws, name='results_ws'),
)