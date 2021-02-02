from django.forms import ModelForm

from .models import Song

class CreateSongForm(ModelForm):
    class Meta:
        model = Song
        exclude = ['owner']
