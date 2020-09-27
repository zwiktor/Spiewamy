from django.shortcuts import render, redirect
from django.http import request, HttpResponse, Http404

from .models import Song, User, SingRoom

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user

def home_view(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'home.html')# pierwsze wejscie na strone

    elif request.method == 'POST':
        username = request.POST['username']#przypisanie danych z httprequest
        is_user = User.objects.get(username=username)
        if is_user:
            return redirect(f'/sing/{username}')
        else:
            raise Http404('Uzytkownik nie istnieje')

def singroom_view(request, username,  *args, **kwargs):
    user_id = User.objects.get(username=username).id

    songroom = SingRoom.objects.get(user_id=user_id)
    if not songroom.song:
        raise Http404('Uzytkownik nie spiewa')
    song = Song.objects.get(id=songroom.song_id)
    return render(request, 'singroom.html', context={'song': song})

## CRUD do obslugiwania piosenek przez uzytkownika


@login_required(login_url='/account/login')
def dashboard_view(request,  *args, **kwargs):
    if request.method == 'GET':
        username = get_user(request)
        songs = Song.objects.filter(owner=username)
        context = {'songs' : songs}
    return render(request, 'dashboard.html', context)


@login_required(login_url='/account/login')
def view_song(request, id,  *args, **kwargs):
    if request.method == 'GET':
        pass


@login_required(login_url='/account/login')
def add_song(request, id,  *args, **kwargs):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass


@login_required(login_url='/account/login')
def edit_song(request, id,  *args, **kwargs):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass


@login_required(login_url='/account/login')
def remove_song(request, id,  *args, **kwargs):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass





