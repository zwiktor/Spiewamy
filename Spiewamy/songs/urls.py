from django.urls import path
from .views import singroom_view, home_view

urlpatterns = [
    path('', home_view),
    path('<str:username>/', singroom_view),
]