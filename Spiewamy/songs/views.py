from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from .models import Song, User

def home_view(request, *args, **kwargs):
    if request.method == 'GET':

        return render(request, 'home.html')
    elif request.method == 'POST':
        username = request.POST['username']
        return redirect(f'/{username}')


def home_song_view(request, *args, **kwargs):
    # tutaj logika chanelsow
    return HttpResponse('this is user webpage')


