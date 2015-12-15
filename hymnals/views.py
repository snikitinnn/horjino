# -*- coding: UTF-8 -*-
from django.shortcuts import get_object_or_404, render
from hymnals.models import Chorus, Song, Hymnal, WS, SongvsWS

def choir(request, chorus_id):
    hymnal_list = Hymnal.objects.extra(where=['chorus_id=%s'], params=[chorus_id])
#    hymnal_list = Hymnal.objects.all()
#    hymnal_list = hymnal_list.filter(chorus_id=chorus_id).order_by('Hymnal_Name')
    chorus = get_object_or_404(Chorus, pk=chorus_id)
    context = {'hymnal_list': hymnal_list, 'chorus':chorus}
    return render(request, 'hymnals/choir.html', context)

def detail(request, hymnal_id):
    selected_song_list = Song.objects.extra(where=['hymnal_id=%s'], params=[hymnal_id])
    hymnal = get_object_or_404(Hymnal, pk=hymnal_id)
    context = {'selected_song_list' : selected_song_list, 'hymnal': hymnal}
    return render(request, 'hymnals/detail.html', context)

def results(request, hymnal_id, song_id):
    song_count = SongvsWS.objects.filter(song_id=song_id).count()
    svsws = SongvsWS.objects.extra(where=['song_id=%s'], params=[song_id])
    date_ws = svsws.extra(select={'ws_id': 'SELECT ws_id FROM hymnals_ws,hymnals_songvsws WHERE hymnals_ws.id = hymnals_songvsws.ws_id'})
    date_list = date_ws.select_related('ws__Date')

    song = get_object_or_404(Song, pk=song_id)
    hymnal = get_object_or_404(Hymnal, pk=hymnal_id)
    context = {'song': song, 'hymnal': hymnal, 'song_count': song_count, 'svsws': svsws, 'date_list': date_list}
    return render(request, 'hymnals/results.html', context)

def alphabet(request):
    alphabet_song_list = Song.objects.all().order_by('Name')
    context = {'alphabet_song_list' : alphabet_song_list}
    return render(request, 'hymnals/alphabet.html', context)

#######################################

def ws(request):
    latest_ws_list = WS.objects.all()
    context = {'latest_ws_list': latest_ws_list}
    return render(request, 'hymnals/ws.html', context)

def detail_ws(request, ws_id):
    selected_songvsws = SongvsWS.objects.extra(where=['ws_id=%s'], params=[ws_id])
    ws = get_object_or_404(WS, pk=ws_id)
    context = {'selected_songvsws': selected_songvsws, 'ws': ws}
    return render(request, 'hymnals/detail_ws.html', context)
# #    selected_songvsws = SongvsWS.objects.filter(ws_id=53)
#     selected_songvsws_list = selected_songvsws.extra(select={'hymnal_id': 'SELECT hymnal_id FROM hymnals_hymnal,hymnals_song WHERE hymnals_song.hymnal_id = hymnals_hymnal.id'
# #    selected_songvsws_list = selected_songvsws.extra(select={'hymnal_id': 'SELECT hymnal_id FROM hymnals_hymnal,hymnals_song, hymnals_songvsws WHERE hymnals_song.hymnal_id = hymnals_hymnal.id AND hymnals_song.id = hymnals_songvsws.song_id'})
# #    selected_songvsws_list = selected_songvsws.select_related('song__hymnal_Hymnal_Name')


# def detail_ws(request, ws_id):
# #    selected_songvsws = SongvsWS.objects.extra(where=['ws_id=%s'], params=[ws_id])
#     selected_songvsws = SongvsWS.objects.filter(ws_id=ws_id)
#     sws = selected_songvsws.values('song_id')
#     s = sws.select_related('song__hymnal_id')
#     h = s.hymnal
#
# #    selected_songvsws_hym = selected_songvsws.extra(select={'hymnal_id': 'SELECT hymnal_id FROM hymnals_hymnal,hymnals_song WHERE hymnals_song.hymnal_id = hymnals_hymnal.id'})
# #    selected_songvsws_list = selected_songvsws_hym.select_related('song__hymnal__Hymnal_Name')
#     ws = get_object_or_404(WS, pk=ws_id)
#     context = {'s': sws, 'h': h, 'ws': ws}
# #    context = {'selected_songvsws_list' : selected_songvsws_list, 'ws': ws}
#     return render(request, 'hymnals/detail_ws.html', context)

def results_ws(request, ws_id, song_id):
    song = get_object_or_404(Song, pk=song_id)
    ws = get_object_or_404(WS, pk=ws_id)
    context = {'song': song, 'ws': ws}
    return render(request, 'hymnals/results_ws.html', context)
