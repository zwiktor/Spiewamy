from django.urls import path
from .views import singroom_view, home_view, dashboard_view, view_song, edit_song, remove_song, add_song, set_song, api_song, api_singroom, api_users, api_user_songs, user_songs

urlpatterns = [
    path('', home_view, name='home'),
    path('sing/<str:username>/', singroom_view),
    path('sing/<str:username>/songs', user_songs, name='userSongs'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('song/set/<int:id>', set_song, name='setSong'),
    # CRUD dla użytkowników
    path('song/add', add_song, name='addSong'),
    path('song/<int:id>', view_song, name='viewSong'),
    path('song/<int:id>/edit', edit_song, name='editSong'),
    path('song/<int:id>/delete', remove_song, name='removeSong'),

    path('api/song/<int:id>', api_song, name='apiSong'),
    path('api/<str:username>', api_singroom, name='apiSingroom'),
    path('api/all/users', api_users, name='apiUsers'),
    path('api/<str:username>/songs', api_user_songs, name='apiUserSongs'),
]