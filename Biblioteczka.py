import random
from hashlib import new
from tabnanny import filename_only
from xml import dom

class Film:


    def play (self):
        print(self.odtworzenia + 1)

    def __init__(self, tytuł, wydanie, gatunek, odtworzenia):
        self.tytuł = tytuł
        self.wydanie = wydanie
        self.gatunek = gatunek
        self.odtworzenia = odtworzenia

    def __str__(self):
        info = self.tytuł + "\n"
        info += self.wydanie + "\n"
        info += self.gatunek + "\n"
        return info

    def __add__(self):
        f = self.odtworzenia + 1
        return self.odtworzenia + 1

Karaiby = Film(tytuł="Karaiby", wydanie="2011", gatunek="thriller", odtworzenia=[300])
Scooby_doo = Film(tytuł="Scooby_Doo", wydanie="2004", gatunek="komedia", odtworzenia=[200])
Dom_strachu = Film(tytuł="Dom_strachu", wydanie="2018", gatunek="kryminalny", odtworzenia=[600])

class Serial(Film):

    def __init__(self, odcinek, sezon, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.odcinek = odcinek
        self.sezon = sezon

    def __str__(self):
        info = self.tytuł + "\n"
        info = self.sezon + "\n"
        info += self.odcinek + "\n"
        return info

Rodzinka = Serial(tytuł="Rodzinka", wydanie="2003", gatunek="komedia", odtworzenia=[400], odcinek="E05", sezon="S03")
Dexter = Serial(tytuł="Dexter", wydanie="2007", gatunek="horror", odtworzenia=[670], odcinek="E04", sezon="S09")
Spongebob = Serial(tytuł="Spongebob", wydanie="2000", gatunek="komedia", odtworzenia=[240], odcinek="E02", sezon="S08")

filmy = Film
serialy = Serial

lista = [Karaiby, Spongebob, Dexter]
get_movies = ["Karaiby", "Scooby_doo", "Dom_strachu"]
get_series = ["Rodzinka", "Spongebob", "Dexter"]

#Funkcja serial oraz film
print(sorted(get_series))
print(sorted(get_movies))
