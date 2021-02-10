from django.test import TestCase
from .models import Song

# class SongTestCase(TestCase):
#     def setUp(self):
#         Song.objects.create(title='Tytul')
#         Song.objects.create(title='IQ', text='''dla ciebie zaciągnę każdy dług
# dla ciebie ściągnę obrączkę
# a jeśli zechcesz przebiję ci serce
# i tryśnie czarna
# czarna ciężka krew
# i wtedy wytrę swoje dłonie
# w czarny ciężki koc
# i zawyję do księżyca
# i zawyję w noc
#
# że miło patrzeć ma miła
# jak rzucasz się jak wij
# jak życie z ciebie ucieka
# jak z oka igły nić
#
# i zajadą tedy po mnie
# czarne wściekłe psy
# wyskoczą chłopy jak konie
# i pochwycą mnie w mig
# i wykręcą moje dłonie
# pęknie kręgów słup
# i zawyję do księżyca
# i zawyję znów
#
# że miło patrzeć ma miła
# jak wijesz się jak wij
# jak życie z ciebie ucieka
# jak z oka igły nić
# i że niczego się nie boję
# i nie zamierzam uciekać
# bo tam na górze nikogo nie ma
# i nikt tam na nas nie czeka''')
#         Song.objects.create(title='Most na krzywej', text='''Wiem
# Pewnie spytacie: Czemu to zrobiłem?
# Czemu znów jestem tu?
# Czemu w pół drogi zawróciłem?
# Jak nic, nie powinno mnie tu być
#
# Wiem
# Zrobiłem tych parę głupstw
# Ale parę głupstw powinno być wybaczone
# Rano usłyszałem głos:
# "Nie jesteś tym który powinien tu być"
# Więc wyruszyłem
#
# Wiem, pewnie spytacie: Czemu to zrobiłem?
# Czy odebrało rozum mi?
# Czemu do zimnej, czarnej rzeki skoczyłem
# W taki cudowny świt?
#
# Wiem
# Zrobiłem tych parę głupstw
# Ale parę głupstw powinno być wybaczone
# Ale powiedziała mi:
# Nie jestem tym, który powinien z nią być
# Więc skoczyłem
#
# Święty Piotrze
# Pewnie spytasz czemu to zrobiłem?
# Czemu stoję tu?
# Czemu targnąłem się z mostu na Krzywej
# W czarny, szalony nurt?
#
# Wiem
# Zrobiłem tych parę głupstw
# ale parę głupstw powinno być wybaczone
# Na Boga, wiem
# Nie jestem tym, który powinien tu być
# Czy mnie rozumiesz?
#
# Ta cisza to za dużo dla mego serca
# Moje serce nie może dłużej tak stać
# Nagle święty Piotr się budzi
# Wstaje, podnosi ręce prosto do nieba:
# "Do diabła, wiem
# Nie jesteś tym, który powinien tu być!
# Do diabła, wiem
# Nie jesteś tym, który powinien tu być!
# Do diabła, wiem
# Nie jesteś tym, który powinien tu być!
# Do diabła, wiem
# Nie jesteś tym, który powinien tu być!
# Do diabła, wiem
# Nie jesteś tym, który powinien tu być!"
# Więc wróciłem''', style='S', play_on='P')
#         Song.objects.create(title='Taka woda byc', text='''taką wodą być,
# co otuli ciebie całą,
# ogrzeje ciało, zmyje resztki parszywego dnia.
# I uspokoi każdy nerw,
# zabawnie pomarszczy dłonie,
# a kiedy zaśniesz wiernie będzie przy twym łóżku stać.
#
# I taką wodą być,
# a nie tą, co żałośnie całą noc tłucze się po oknie.
# Wczoraj... wczoraj...
#
# I taką wodą być,
# co nawilży twoje wargi,
# uwolni kąciki ust, gdy przyłożysz je do szklanki.
# I czarną kawę zmieni w płyn,
# kiedy dni skute lodem.
# A kiedy z nieba poleje się żar, poczęstuje chłodem.
#
# I taką wodą być,
# a nie tą, co żałośnie całą noc w gardle pali ogniem.
# Wczoraj... wczoraj
# nie liczy się,
# bo wczoraj,
# bo wczoraj...
#
# I taką wodą być,
# a nie tą co żałośnie całą noc w gardle pali ogniem.
# Wczoraj... wczoraj
# nie liczy się,
# Wczoraj... wczoraj
# nie liczy się,
# bo wczoraj...
# bo wczoraj... nie było, nie...''', play_on='A', style='F')
#         Song.objects.create(title='Sa momenty takie', text='''Są momenty takie, że o wszystkim zapominam
# Co to są rzeczy ważne: zdrowie, rodzina
# Wszystko wtedy wokół zwalnia, stygnie i staje
# Jakaś dziwna siła tuli mnie i uspokaja
#
# Bo żyję sobie wtedy
# Żyję sobie wtedy
# Żyję sobie wtedy
# Marzeniami
#
# O dalekich podróżach
# I o wielkich wygranych
# O dalekich podróżach
# No i o wielkich wygranych
#
# I że kiedyś spotkam ufo
# I tak zapytany
# Jak się tutaj mamy
# Wszystko wyśpiewam im
#
# Że ciężko nam tu żyć, ale że kochamy życie
# Chociaż rzadko sprawiedliwe i że rządzą nami świnie
# A tych kilku królów, których ściskamy w kieszeniach
# Niewiele uszyjesz z tego
# Ale choćbyś beczał muszą starczyć do pierwszego
#
# A kiedy mamy wolne to lubimy się zabawić
# Lubimy dobry seks, lubimy wypić i zapalić
#
# A kiedy zostajemy sami
# Kiedy zostajemy sami
# Kiedy zostajemy sami
# Żyjemy marzeniami
#
# O dalekich podróżach
# I o wielkich wygranych
# O dalekich podróżach
# No i o wielkich wygranych
# O szybkich samochodach
# I o dziewczynach z żurnali
# O dalekich podróżach
# No i o wielkich wygranych''', play_on='G')
#         Song.objects.create(title='Made in china', text='''Ręce, serce, głowa
# szyja, piersi, dolna część tułowia
# Kochana!
# Nie wszystko jest made in China
# Kochana!
# Wolna wolność słowa, w dłoniach mleczna droga
# Koślawy krok o brzasku, w oczach słone ziarna
#
# Kochana! Kochana!
# nie wszystko jest made in China
# Kochana!
#
# Na twarz źródlana woda, wojna atomowa
# Tysiące słów na wiatr, złego dobre końce
#
# Kochana! Kochana!
# Nie wszystko jest made in China
# Kochana!
# Nie wszystko jest made in China''', style='C')
#
#
#     def test_song_is_created(self):
#         '''object created with defaults'''
#         song = Song.objects.get(title='Tytul')
#         songs = Song.objects.all()
#         self.assertEqual(song.play_on, 'G')
#         self.assertEqual(song.get_play_on_display(), 'Gitara') ## This is awesome, how can i display value from choices
#         self.assertEqual(song.style, 'P')
#         self.assertEqual(song.text, Song().text)
#         self.assertEqual(songs.count(), 6)
#
#     def test_song_str(self):
#         song = Song.objects.get(title='Tytul')
#         self.assertEqual(song.title, song.__str__())