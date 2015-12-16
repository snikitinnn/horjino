# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
from hymnals import views

urlpatterns = patterns('',
    url(r'^choir/(?P<chorus_id>\d+)/$', views.choir, name='choir'),
    url(r'^(?P<hymnal_id>\d+)/$', views.detail, name='detail'),
    url(r'^alphabet/$', views.alphabet, name='alphabet'),
    url(r'^(?P<hymnal_id>\d+)/(?P<song_id>\d+)/$', views.results, name='results'),
    url(r'^song/(?P<song_id>\d+)/$', views.results_song, name='song'),
    url(r'^ws/$', views.ws, name='ws'),
    url(r'^ws/(?P<ws_id>\d+)/$', views.detail_ws, name='detail_ws'),
    url(r'^ws/(?P<ws_id>\d+)/(?P<song_id>\d+)/$', views.results_ws, name='results_ws'),
#    url(r'^(?P<ws_id>\d+)/$', views.ws, name='ws'),
)