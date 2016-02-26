# -*- coding: UTF-8 -*-

import os
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from forms import SearchForm
from models import Chorus, Song, Hymnal, WS, SongvsWS
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
        selected_song_list = song_list.order_by('Page_Score')
    else:
        selected_song_list = song_list.order_by('Name')
    hymnal = get_object_or_404(Hymnal, pk=hymnal_id)
    context = {'selected_song_list' : selected_song_list, 'hymnal': hymnal, 'order' : order}
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

def results_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    singing_list = SongvsWS.objects.filter(song_id=song_id).order_by('-ws__Date')
    file_name = 'lyrics/'+str(song_id)+'.html'
    context = {'singing_list':singing_list, 'song': song, 'hymnal': song.hymnal}

    if os.path.exists('hymnals/templates/'+file_name):
        return render(request, file_name, context)
    else:
        return render(request, 'lyrics/0.html', context)

def lyrics(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'hymnals/lyrics.html', {'song': song})

#####################################

def alphabet(request, order):
    alphabet_song_list = Song.objects.values('id','Name','hymnal__Hymnal_Name','Page_Score','hymnal__icon','accords')
    if order == 'p':
        alphabet_song_list = alphabet_song_list.order_by('hymnal__Hymnal_Name','Name')
    else:
        alphabet_song_list = alphabet_song_list.order_by('Name')

    context = {'alphabet_song_list' : alphabet_song_list, 'order' : order}
    return render(request, 'hymnals/alphabet.html', context)

def alphabet_chorus(request, chorus_id):
    alphabet_song_list = Song.objects.select_related('hymnal__chorus_id')
    alphabet_song_list = alphabet_song_list.extra(where=['chorus_id = %s'], params=[chorus_id])
    alphabet_song_list = alphabet_song_list.values('id','Name','hymnal__Hymnal_Name','Page_Score','hymnal__icon')
    alphabet_song_list = alphabet_song_list.order_by('Name')
    context = {'alphabet_song_list' : alphabet_song_list}
    return render(request, 'hymnals/alphabet.html', context)

#######################################

def ws(request):
    cur_date = timezone.now()
    ws_list = WS.objects.values('id','Date','chorus__name','Event')
    context = {'ws_list': ws_list, 'cur_date':cur_date}
    return render(request, 'hymnals/ws.html', context)

def ws_chorus(request, chorus_id):
    cur_date = timezone.now()
    ws_list = WS.objects.extra(where=['chorus_id=%s'], params=[chorus_id])
    ws_list = ws_list.values('id','Date','Event')
    context = {'ws_list': ws_list, 'cur_date':cur_date}
    return render(request, 'hymnals/ws.html', context)

def ws_last(request):
#    cur_date = timezone.now()
    cur_date = date.today()
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
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=%s.pdf' %filename
        return response
    pdf.closed


