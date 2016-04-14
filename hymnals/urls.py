# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
from hymnals import views

urlpatterns = patterns('',
    url(r'^choir/(?P<chorus_id>\d+)/$', views.choir, name='choir'),

    url(r'^(?P<hymnal_id>\d+)/(?P<order>\D+)/$', views.detail, name='detail'),
#    url(r'^(?P<hymnal_id>\d+)/(?P<song_id>\d+)/$', views.results, name='results'),

    url(r'^song/(?P<song_id>\d+)/$', views.results_song, name='song'),
    url(r'^song/lyrics/(?P<song_id>\d+)/$', views.lyrics, name='lyrics'),
    url(r'^song/pdf/(?P<song_id>\d+)$', views.file_view, name='pdf'),

    url(r'^alphabet/(?P<chorus_id>\d+)/(?P<order>\D+)/$', views.alphabet, name='alphabet'),
    url(r'^alphabet/chorus/(?P<chorus_id>\d+)/$', views.alphabet_chorus, name='alphabet_chorus'),

    url(r'^ws/(?P<chorus_id>\d+)/$', views.ws, name='ws'),
    url(r'^ws/last/(?P<oneday>\d+)/$', views.ws_last, name='ws_last'),
    url(r'^ws/chorus/(?P<chorus_id>\d+)/$', views.ws_chorus, name='ws_chorus'),
    url(r'^ws/detail/(?P<ws_id>\d+)/$', views.detail_ws, name='detail_ws'),
#    url(r'^ws/(?P<ws_id>\d+)/(?P<song_id>\d+)/$', views.results_ws, name='results_ws'),

    url(r'^search/$', views.search, name='search'),
    url(r'^found/$', views.found, name='found'),
#    url(r'^findform/(?P<findname>\d+)/$', views.findform, name='findform'),
    url(r'^search/findform/$', views.findform, name='findform'),

    url(r'^topic/chorus/(?P<chorus_id>\d+)/$', views.topic_chorus, name='topic_chorus'),
    url(r'^topic/chorus/(?P<chorus_id>\d+)/(?P<topic_id>\d+)/$', views.detail_topic, name='detail_topic'),
    url(r'^songbyws/(?P<chorus_id>\d+)/$', views.songbyws, name='songbyws'),
    url(r'^songbyws/one/(?P<chorus_id>\d+)/(?P<ws_id>\d+)/$', views.songbyws_one, name='songbyws_one'),
#    url(r'^song/lyrics/(?P<song_id>\d+)/$', views.lyrics, name='lyrics'),
)

#   TO DO:
#   todo whole <tr> - link for ws, for example
#   todo display fixed button at the bootom
#   FIX ME:
