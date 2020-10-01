from django.shortcuts import render, redirect
from django.http import request, HttpResponse, Http404, JsonResponse

from .serializers import SongSerializer
from .forms import CreateSongForm
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

    singroom = SingRoom.objects.get(user_id=user_id)
    if not singroom.song:
        raise Http404('Uzytkownik nie spiewa')
    song = Song.objects.get(id=singroom.song_id)
    return render(request, 'singroom.html', context={'song': song})

## CRUD do obslugiwania piosenek przez uzytkownika


@login_required(login_url='/account/login')
def dashboard_view(request,  *args, **kwargs):
    if request.method == 'GET':
        username = get_user(request)
        singroom = SingRoom.objects.get(user=username)
        songs = Song.objects.filter(owner=username)
        context = {'songs' : songs, 'singroom': singroom}
        return render(request, 'dashboard.html', context)


@login_required(login_url='/account/login')
def set_song(request, id, *args, **kwargs):
    if request.method == 'GET':
        user = get_user(request)
        song = Song.objects.get(id=id)
        singroom = SingRoom.objects.get(user=user)
        singroom.song = song
        singroom.save()
        return redirect('dashboard')


@login_required(login_url='/account/login')
def view_song(request, id,  *args, **kwargs):
    if request.method == 'GET':
        song = Song.objects.get(id=id)
        context = {'song': song}
        return render(request, 'song.html', context)


@login_required(login_url='/account/login')
def add_song(request,  *args, **kwargs):
    if request.method == 'GET':
        form = CreateSongForm()
        context = {'form': form}
        return render(request, 'addSong.html', context)
    elif request.method == 'POST':
        ## Tutaj sprawdzę możliwości wyciągnięcia danych z post data !!!!!!!!!!!!!!!
        form = CreateSongForm(request.POST) # tworzy instancje formularza z przesłanymi danymi
        if form.is_valid():# sprawdza czy formularz zgadza się z forms.py -> models.py
            title = form.cleaned_data['title'] # to wyciąga czyste dane z inputa
            text = form.cleaned_data['text']
            style = form.cleaned_data['style']
            play_on= form.cleaned_data['play_on']
            user = get_user(request)
            song = Song.objects.create(title=title, text=text, style=style, play_on=play_on, owner=user)
            song.save()
            return redirect('dashboard') # dziala przekierowywanie po name w url - to ułatwia poruszanie się po strukturze aplikacji


@login_required(login_url='/account/login')
def edit_song(request, id,  *args, **kwargs):
    if request.method == 'GET':
        song = Song.objects.get(id=id)
        form = CreateSongForm(instance=song)# mozna uzywac instance do podkladnia danych z modeli
        context = {'form': form}
        return render(request, 'editSong.html', context)
    elif request.method == 'POST':
        form = CreateSongForm(request.POST)  # tworzy instancje formularza z przesłanymi danymi
        if form.is_valid():  # sprawdza czy formularz zgadza się z forms.py -> models.py
            title = form.cleaned_data['title']  # to wyciąga czyste dane z inputa
            text = form.cleaned_data['text']
            style = form.cleaned_data['style']
            play_on = form.cleaned_data['play_on']
            # user = get_user(request) to raczej w edycji nie jest potrzebne
            song = Song.objects.get(id=id)
            song.title = title
            song.text = text
            song.style = style
            song.play_on = play_on
            song.save()
            return redirect('dashboard')


@login_required(login_url='/account/login')
def remove_song(request, id,  *args, **kwargs):
    if request.method == 'GET':
        song = Song.objects.get(id=id)
        song.delete()
        return redirect('dashboard')


def api_song(request, id, *args, **kwargs):
    if request.method == 'GET':
        song = Song.objects.get(id=id)
        serializer = SongSerializer(instance=song)
        return JsonResponse(serializer.data)



def api_singroom(request, username, *args, **kwargs):
    if request.method == 'GET':
        user_id = User.objects.get(username=username).id
        song_id = SingRoom.objects.get(user_id=user_id).id
        song = Song.objects.get(id=song_id)
        serializer = SongSerializer(instance=song)
        return JsonResponse(serializer.data)



