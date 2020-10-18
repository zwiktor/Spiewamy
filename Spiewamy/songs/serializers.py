from rest_framework import serializers
from .models import Song, User

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'text', 'play_on', 'style', 'created', 'owner']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']