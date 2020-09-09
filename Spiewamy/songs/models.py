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
    style = models.CharField(max_length=1, choices=STYLE_CHOICES, null=True)
    play_on = models.CharField(max_length=1, choices=INSTRUMENT_CHOICES, null=True)
    created = models.DateField(auto_now_add=True)
    # TO DO maximum dwa gantunki muzyki do wyboru

    def __str__(self):
        return self.title
