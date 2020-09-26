from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class Song(models.Model):
    INSTRUMENT_GUITAR = 'G'
    INSTRUMENT_ACCORDION = 'A'
    INSTRUMENT_PIANO = 'P'
    INSTRUMENT_CHOICES = [
        (INSTRUMENT_GUITAR, 'Gitara'),
        (INSTRUMENT_ACCORDION, 'Akordeon'),
        (INSTRUMENT_PIANO, 'Pianino'),

    ]

    STYLE_POP = 'P'
    STYLE_ROCK = 'R'
    STYLE_SHANTIES = 'S'
    STYLE_CLASSIC = 'C'
    STYLE_FOLK = 'F'
    STYLE_CHOICES = [
        (STYLE_POP, 'Popularna'),
        (STYLE_ROCK, 'Rock'),
        (STYLE_SHANTIES, 'Szanty'),
        (STYLE_CLASSIC, 'Klasyczna'),
        (STYLE_FOLK, 'Biesiada'),
    ]


    title = models.CharField(max_length=128)
    text = models.TextField(default='This is plain text')
    '''
    Zapisywac tekst piosenki tak zeby posidal biale znaki(\n, \t, \r).
    '''
    style = models.CharField(max_length=1, choices=STYLE_CHOICES, default='P')
    play_on = models.CharField(max_length=1, choices=INSTRUMENT_CHOICES, default='G')
    created = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    '''
    Przypisywac uzytkownika ktory dodal te piosenke. 
    Pozwoli to na posiadanie piosenke dodanych przez uzytkownia
    '''
    # TO DO maximum dwa gantunki muzyki do wyboru

    class Meta:

        ordering = ['title']

    def __str__(self):
        return self.title

class SingRoom(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    song = models.OneToOneField(Song, null=True, on_delete=models.SET_NULL)

    #user.username == song.owner.username

    def __str__(self):
        if self.song:
            return f'{self.user.username}, {self.song.title}'
        else:
            return self.user.username