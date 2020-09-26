from django.urls import path
from .views import home_song_view, home_view

urlpatterns = [
    path('', home_view),
    path('<str:username>/', home_song_view),
]