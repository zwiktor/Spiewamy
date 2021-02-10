from django.shortcuts import render, redirect
from django.http import request, HttpResponse, Http404

from .serializers import SongSerializer, UserSerializer
from .forms import CreateSongForm
from .models import Song, User, SingRoom, ProposeSongs

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from django.contrib import messages

def home_view(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'home.html')# pierwsze wejscie na strone

    elif request.method == 'POST':
        username = request.POST['username']#przypisanie danych z httprequest
        user = User.objects.filter(username=username)
        if user:
            return redirect(f'/sing/{username}')
        else:
            raise Http404('Uzytkownik nie istnieje')

def singroom_view(request, username,  *args, **kwargs):
    user = User.objects.get(username=username)
    if not user:
        raise Http404('Niema Uzytkownika')
    user_id = user.id
    singroom = SingRoom.objects.get(user_id=user_id)
    if not singroom.song:
        raise Http404('Uzytkownik nie spiewa')
    song = Song.objects.get(id=singroom.song_id)
    return render(request, 'singroom.html', context={'song': song})

def user_songs(request, username,  *args, **kwargs):
    if request.method == 'GET':
        user = User.objects.get(username=username)
        songs = Song.objects.filter(owner=user)
        context = {'songs': songs, 'username': user}
        return render(request, 'userSongs.html', context=context)

    if request.method == 'POST':
        new_song = request.POST.get('new_song')
        if new_song or new_song == '':
            user = User.objects.get(username=username)
            PropSong = ProposeSongs.objects.create(name=new_song, user=user)
            messages.info(request, f'Gratulacje, zaproponowałeś piosenkę {new_song}')
            return redirect('singroom', username)
        song_id_with_noise = request.POST.get('song')
        song_id = song_id_with_noise.split('?')[1]
        song = Song.objects.get(id=song_id)
        song.votes += 1
        song.save()
        messages.info(request, 'Gratulacje, zaglosowales na piosenkę')
        return redirect('singroom', username)

@login_required(login_url='/account/login')
def dashboard_view(request,  *args, **kwargs):
    if request.method == 'GET':
        username = get_user(request)
        singroom = SingRoom.objects.get(user=username)
        songs = Song.objects.filter(owner=username)
        context = {'songs' : songs, 'singroom': singroom}
        return render(request, 'dashboard.html', context)

    if request.method == 'POST':
        songs_for_votes = Song.objects.filter(owner=get_user(request))
        for song in songs_for_votes:
            print(song.votes)
            song.votes = 0
            song.save()
        print('haloh alo')
        return redirect('dashboard')


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
            text = form.cleaned_data['text'].replace(' ', '&nbsp;')
            text = text.replace('\r\n', '<br>')
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
        form = CreateSongForm(instance=song)
        # form.cleaned_data['text'].replace('<br>', '\r\n').replace('&nbsp;', ' ')
        context = {'form': form}
        return render(request, 'editSong.html', context)
    elif request.method == 'POST':
        form = CreateSongForm(request.POST)  # tworzy instancje formularza z przesłanymi danymi
        if form.is_valid():  # sprawdza czy formularz zgadza się z forms.py -> models.py
            title = form.cleaned_data['title']  # to wyciąga czyste dane z inputa
            text = form.cleaned_data['text'].replace('\r\n', '<br>')
            text = text.replace('\s', '&nbsp;')
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


@login_required(login_url='/account/login')
def remove_song_votes(request, id,  *args, **kwargs):
    if request.method == 'GET':
        song = Song.objects.get(id=id)
        song.votes = 0
        song.save()
        return redirect('dashboard')

@api_view(['GET'])
def api_song(request, id, *args, **kwargs):
    if request.method == 'GET':
        song = Song.objects.get(id=id)
        serializer = SongSerializer(instance=song)
        return Response(serializer.data)


@api_view(['GET'])
def api_singroom(request, username, *args, **kwargs):
    if request.method == 'GET':
        user = User.objects.get(username=username)
        if user.singroom.song:
            song_id = user.singroom.song.id
        else:
            return Response({'id': '-1'}, status=200)
        song = Song.objects.get(id=song_id)
        serializer = SongSerializer(instance=song)
        return Response(serializer.data, status=200)


@api_view(['GET'])
def api_user_songs(request, username, *args, **kwargs):
    if request.method == 'GET':
        user = User.objects.get(username=username)
        songs = Song.objects.filter(owner=user)
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=200)


@api_view(['GET'])
def api_users(request, *args, **kwargs):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=200)
