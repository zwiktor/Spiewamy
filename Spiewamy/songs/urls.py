from django.urls import path
from .views import home_song_view, home_view

urlpatterns = [
    path('song/', home_song_view),
    path('', home_view),
]