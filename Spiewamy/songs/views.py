from django.shortcuts import render
from django.http import request, HttpResponse
from .models import Song

def home_view(request, *args, **kwargs):
    # po wpisaniu uzytkownika przekierowanie na strone z jego piosenka
    return HttpResponse(f'formatka do wpisania uzytkownika')

def home_song_view(request, *args, **kwargs):
    song = Song.objects.get(title='123')

    return render(request, 'home.html')
