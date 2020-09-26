from django.shortcuts import render, redirect
from django.http import request, HttpResponse, Http404
from .models import Song, User, SingRoom

def home_view(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'home.html')# pierwsze wejscie na strone

    elif request.method == 'POST':
        username = request.POST['username']#przypisanie danych z httprequest
        is_user = User.objects.get(username=username)
        if is_user:
            return redirect(f'/{username}')
        else:
            raise Http404('Uzytkownik nie istnieje')

def singroom_view(request, username,  *args, **kwargs):
    user_id = User.objects.get(username=username).id

    songroom = SingRoom.objects.get(user_id=user_id)
    if not songroom.song:
        raise Http404('Uzytkownik nie spiewa')
    song = Song.objects.get(id=songroom.song_id)
    return render(request, 'singroom.html', context={'song': song})


