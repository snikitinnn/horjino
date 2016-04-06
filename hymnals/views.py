# -*- coding: UTF-8 -*-

import os
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from forms import SearchForm
from models import Chorus, Song, Hymnal, WS, SongvsWS, Topic, TopicSong
from datetime import date
from pytils import translit

def choir(request, chorus_id):
#    hymnal_list = Hymnal.objects.extra(where=['chorus_id=%s'], params=[chorus_id])
    hymnal_list = Hymnal.objects.filter(chorus_id=chorus_id, active=True).order_by('id')
    chorus = get_object_or_404(Chorus, pk=chorus_id)
    context = {'hymnal_list': hymnal_list, 'chorus':chorus}
    return render(request, 'hymnals/choir.html', context)

# hymnals
def detail(request, hymnal_id, order):
    song_list = Song.objects.extra(where=['hymnal_id=%s'], params=[hymnal_id])
    if order == 'p':
        selected_song_list = song_list.order_by('Page_Score','Name')
    elif order == 'n':
        selected_song_list = song_list.order_by('Name','Page_Score')
    elif order == 'f':
        selected_song_list = song_list.order_by('accords','Name')
    elif order == 's':
        selected_song_list = song_list.order_by('over','Name')
    hymnal = get_object_or_404(Hymnal, pk=hymnal_id)
    context = {'selected_song_list' : selected_song_list, 'hymnal': hymnal, 'order' : order}
    return render(request, 'hymnals/detail.html', context)

# def results(request, hymnal_id, song_id):
#     song_count = SongvsWS.objects.filter(song_id=song_id).count()
#     svsws = SongvsWS.objects.extra(where=['song_id=%s'], params=[song_id])
#     date_ws = svsws.extra(select={'ws_id': 'SELECT ws_id FROM hymnals_ws,hymnals_songvsws WHERE hymnals_ws.id = hymnals_songvsws.ws_id'})
#     date_list = date_ws.select_related('ws__Date')
#
#     song = get_object_or_404(Song, pk=song_id)
#     hymnal = get_object_or_404(Hymnal, pk=hymnal_id)
#     context = {'song': song, 'hymnal': hymnal, 'song_count': song_count, 'svsws': svsws, 'date_list': date_list}
#     return render(request, 'hymnals/results.html', context)

def results_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    singing_list = SongvsWS.objects.filter(song_id=song_id).order_by('-ws__Date')
    topic_list = TopicSong.objects.filter(song_id=song_id).order_by('topic__name')
#    context = {'singing_list':singing_list, 'topic_list':topic_list, 'song': song, 'hymnal': song.hymnal}
    context = {'singing_list':singing_list, 'topic_list':topic_list, 'song': song}

    file_name = 'lyrics/'+str(song_id)+'.html'
    if os.path.exists('hymnals/templates/'+file_name):
        return render(request, file_name, context)
    else:
        return render(request, 'lyrics/0.html', context)

def lyrics(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'hymnals/lyrics.html', {'song': song})

#####################################

def alphabet(request, order):
    alphabet_song_list = Song.objects.values('id','Name','hymnal__Hymnal_Name','Page_Score','hymnal__icon','accords','over')
    if order == 'h':
        alphabet_song_list = alphabet_song_list.order_by('hymnal__Hymnal_Name','Page_Score','Name')
    elif order == 'p':
        alphabet_song_list = alphabet_song_list.order_by('hymnal__Hymnal_Name','Name')
    elif order == 'n':
        alphabet_song_list = alphabet_song_list.order_by('Name','Page_Score')
    elif order == 's':
        alphabet_song_list = alphabet_song_list.order_by('over','Name')
    elif order == 'f':
        alphabet_song_list = alphabet_song_list.order_by('accords','Name')

    context = {'alphabet_song_list' : alphabet_song_list, 'order' : order, 'chorus':None}
    return render(request, 'hymnals/alphabet.html', context)

def alphabet_chorus(request, chorus_id):
    alphabet_song_list = Song.objects.select_related('hymnal__chorus_id')
    alphabet_song_list = alphabet_song_list.extra(where=['chorus_id = %s'], params=[chorus_id])
    alphabet_song_list = alphabet_song_list.values('id','Name','hymnal__Hymnal_Name','Page_Score','hymnal__icon','accords','over')
    alphabet_song_list = alphabet_song_list.order_by('Name')
    chorus = get_object_or_404(Chorus, pk=chorus_id)
    context = {'alphabet_song_list' : alphabet_song_list, 'chorus':chorus}
    return render(request, 'hymnals/alphabet.html', context)

#######################################

def ws(request):
    cur_date = timezone.now()
    ws_list = WS.objects.values('id','Date','chorus__name','Event')
    context = {'ws_list': ws_list, 'cur_date':cur_date, 'chorus':None}
    return render(request, 'hymnals/ws.html', context)

def ws_chorus(request, chorus_id):
    cur_date = timezone.now()
    ws_list = WS.objects.extra(where=['chorus_id=%s'], params=[chorus_id])
    ws_list = ws_list.values('id','Date','Event')
    chorus = get_object_or_404(Chorus, pk=chorus_id)
    context = {'ws_list': ws_list, 'cur_date':cur_date, 'chorus':chorus}
    return render(request, 'hymnals/ws.html', context)

def ws_last(request, oneday):
#    cur_date = timezone.now()
    cur_date = date.today()
    if oneday == 1:
        coming_ws_list = WS.objects.extra(where=['Date=%s'], params=[cur_date])
    else:
        coming_ws_list = WS.objects.extra(where=['Date>=%s'], params=[cur_date])
    coming_ws_list = coming_ws_list.values('id','Date','chorus__name','Event')
    context = {'ws_list': coming_ws_list, 'cur_date':cur_date}
    return render(request, 'hymnals/ws.html', context)


#######################################

def detail_ws(request, ws_id):
    ws = get_object_or_404(WS, pk=ws_id)
#    songvsws_list = SongvsWS.objects.filter(ws_id=ws_id)
    songvsws_list = SongvsWS.objects.extra(where=['ws_id=%s'], params=[ws_id])
    songvsws_list = songvsws_list.order_by('sequence')
    context = {'ws':ws, 'songvsws_list':songvsws_list}
    return render(request, 'hymnals/detail_ws.html', context)

def results_ws(request, ws_id, song_id):
    song = get_object_or_404(Song, pk=song_id)
    ws = get_object_or_404(WS, pk=ws_id)
    context = {'song': song, 'ws': ws}
    return render(request, 'hymnals/results_ws.html', context)

############################################
def topic_chorus(request, chorus_id):
    chorus = get_object_or_404(Chorus, pk=chorus_id)
    topic_list = Topic.objects.all()
    topic_list = topic_list.extra(select={'song_count':'SELECT COUNT(*) FROM hymnals_topicsong, hymnals_hymnal, hymnals_song WHERE hymnals_topicsong.topic_id = hymnals_topic.id AND hymnals_hymnal.id = hymnals_song.hymnal_id AND hymnals_song.id=hymnals_topicsong.song_id AND hymnals_hymnal.chorus_id = %s' %chorus_id})
    context = {'topic_list' : topic_list, 'chorus' : chorus}
    return render(request, 'hymnals/topic_chorus.html', context)

def detail_topic(request, chorus_id, topic_id):
    chorus = get_object_or_404(Chorus, pk=chorus_id)
    topic = get_object_or_404(Topic, pk=topic_id)
    song_list = TopicSong.objects.all()
    song_list = song_list.select_related('song','song__hymnal')#,'song__Page','song__over','song__accords')
    song_list = song_list.extra(where=['topic_id=%s'], params=[topic_id])
    song_list = song_list.order_by('song__Name')
#    song_list = song_list.prefetch_related('song')
#    song_list = song_list.extra(where=['song__hymnal_chorus=%s'], params=[chorus_id]) #prefetch_related('song')
#    song_list= TopicSong.objects.extra(select={'ch': 'SELECT hymnals_hymnal.chorus_id FROM hymnals_hymnal WHERE hymnals_hymnal.chorus_id = chorus_id'})
    context = {'song_list' : song_list, 'topic' : topic, 'chorus' : chorus}
    return render(request, 'hymnals/detail_topic.html', context)

########################################

def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        # кривой ход, потомучто blank=True не срабатывает
        # if form.Name == '':
        #     form.Name = 'NULL'
        # if form.Authors == '':
        #     form.Name = 'NULL'
        # if form.Name != 'NULL' and form.Name != 'NULL':
        if form.is_valid():
            search = form.save(commit=False)

            song_list = Song.objects.values('id','Name', 'hymnal__Hymnal_Name','Page_Score','hymnal__icon')
            # if form.Name != 'NULL':
            #     selected_song_list = song_list.filter(Name__contains=search.Name)
            # elif form.Authors != 'NULL':
            #     selected_song_list = song_list.filter(Authors__contains=search.Authors)
            # else:
            #     selected_song_list = song_list.filter(Name__contains=search.Name, Authors__contains=search.Authors)

            #selected_song_list = [name_song_list, authors_song_list,]
            selected_song_list = song_list.filter(Name__contains=search.Name)

            # if search.order == 'p':
            selected_song_list = selected_song_list.order_by('hymnal__Hymnal_Name','Name')
            # else:

            # selected_song_list = selected_song_list.order_by('Name')
            context = {'selected_song_list' : selected_song_list}
            return render (request, 'hymnals/found.html', context)
    else:
        form = SearchForm
    return render (request, 'hymnals/search.html', {'form':form})

def found(request):
    return render (request, 'hymnals/found.html', search)

def findform(request):
    return render (request, 'hymnals/findform.html' )

from django.http import HttpResponse
def file_view(request, song_id):
    song = get_object_or_404(Song, pk=song_id) # output is __unicode__
    filename = translit.slugify(unicode(song.Name))
    with open('static/pdf/' + str(song_id) + '.pdf', 'rb') as pdf:
#    with open('/home/users/s/snikitinnn/domains/snikitinnn.myjino.ru/static/pdf/' + str(song_id) + '.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=%s.pdf' %filename
        return response
    pdf.closed


def songbyws(request, chorus_id):

    song_list = Song.objects.select_related('hymnal__chorus')
    song_list = song_list.extra(where=['chorus_id = %s'], params=[chorus_id])
    song_list = song_list.order_by('Name')
    song_list = song_list.extra(select={'song_count':'True'})
    song_len = len(song_list)

    ws_list = WS.objects.filter(chorus_id=chorus_id).order_by('time')
    ws_len = len(ws_list)
    if ws_len > 20:
        ws_list = ws_list[ws_len-20:ws_len]
        ws_len = 20
    ws_len += 1 # 1st for songname and last for flag of number of sung songs
    ws_time = ws_list[0].time

    ws_row = [0 for j in xrange(0, ws_len)]
    song_table = [ws_row for i in xrange(0, song_len)]

    sws_list_chorus = SongvsWS.objects.all()
    sws_list_chorus = sws_list_chorus.prefetch_related('ws__chorus')
    sws_list_chorus = sws_list_chorus.extra(where=['chorus_id = %s'], params=[chorus_id])
    sws_list_chorus = sws_list_chorus.extra(where=['time >= %s'], params=[ws_time])

#    from django.db import connection,transaction
#    cursor = connection.cursor()
#    cursor.execute('SELECT hymnals_songvsws.id, hymnals_songvsws.ws_id, hymnals_ws.chorus_id FROM hymnals_songvsws, hymnals_ws WHERE hymnals_ws.id = hymnals_songvsws.ws_id AND hymnals_ws.chorus_id=5')
#    sws_list_chorus = cursor.fetchall()
#    cursor.execute('SELECT hymnals_song.Name FROM hymnals_ws INNER JOIN hymnals_songvsws ON hymnals_ws.id = hymnals_songvsws.ws_id INNER JOIN hymnals_songvsws ON hymnals_song.id = hymnals_songvsws.song_id WHERE hymnals_ws.chorus_id = 5 ORDER BY hymnals_ws.time GROUP BY hymnals_song.Name')
#    cursor.execute('SELECT hymnals_song.Name FROM hymnals_ws, hymnals_song, hymnals_songvsws WHERE hymnals_ws.id = hymnals_songvsws.ws_id AND hymnals_song.id = hymnals_songvsws.song_id AND hymnals_ws.chorus_id = 5 ORDER BY hymnals_ws.time GROUP BY hymnals_song.Name')

    song_i = 0
    for song in song_list:
        songid = song.id

        sws_list = sws_list_chorus.extra(where=['song_id=%s'], params=[songid])
        sws_list = sws_list.order_by('ws__time')
        song.song_count = len(sws_list)

        i = 0
        ws_row = [0 for j in xrange(0, ws_len)]
        ws_row[i] = song
        for ws in ws_list:
            i += 1
            f_sws = ws.Supper
            for sws in sws_list:
                if sws.ws_id == ws.id:
                    f_sws = 2
                    break
            ws_row[i] = f_sws

        song_table[song_i] = ws_row
        song_i += 1
    chorus = get_object_or_404(Chorus, pk=chorus_id)
    context = {'song_table':song_table, 'ws_list' : ws_list, 'chorus' : chorus}
    return render(request, 'hymnals/songbyws.html', context)