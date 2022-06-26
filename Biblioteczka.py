from lib2to3.pgen2.pgen import generate_grammar
import random
from hashlib import new
from tabnanny import filename_only
from xml import dom

class Film:

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

    def __repr__(self):
        return repr (self.odtworzenia)

Karaiby = Film(tytuł="Karaiby", wydanie="2011", gatunek="thriller",odtworzenia=300)
Scooby_doo = Film(tytuł="Scooby_Doo", wydanie="2004", gatunek="komedia", odtworzenia=200)
Dom_strachu = Film(tytuł="Dom_strachu", wydanie="2018", gatunek="kryminalny", odtworzenia=600)

class Serial(Film):

    def __init__(self, odcinek, sezon, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.odcinek = odcinek
        self.sezon = sezon

    def __str__(self):
        info = self.wydanie + "\n"
        info += self.gatunek + "\n"
        info += self.tytuł + "\n"
        info += self.sezon + "\n"
        info += self.odcinek + "\n"
        return info

Rodzinka = Serial(tytuł="Rodzinka", wydanie="2003", gatunek="komedia", odtworzenia=400, odcinek="E05", sezon="S03")
Dexter = Serial(tytuł="Dexter", wydanie="2007", gatunek="horror", odtworzenia=670, odcinek="E04", sezon="S09")
Spongebob = Serial(tytuł="Spongebob", wydanie="2000", gatunek="komedia", odtworzenia=240, odcinek="E02", sezon="S08")

lista = (Karaiby, Scooby_doo, Dom_strachu, Rodzinka, Dexter, Spongebob)
filmy = Film
serialy = Serial

#FUNKCJA PLAY
play = Karaiby.odtworzenia +1
play1 = Dom_strachu.odtworzenia +1
play2 = Scooby_doo.odtworzenia +1
play3 = Spongebob.odtworzenia +1
play4 = Dexter.odtworzenia +1
play5 = Rodzinka.odtworzenia +1

#GENERATE_VIEWS
widownia = Karaiby.odtworzenia + random.randint(1, 100)
widowniax10 = Karaiby.odtworzenia + random.randint(1, 100) * 10


#FUNKCJA GET SERIES, GET MOVIES
get_movies = ["Karaiby", "Scooby_doo", "Dom_strachu"]
get_series = ["Rodzinka", "Spongebob", "Dexter"]

print(sorted(get_series))
print(sorted(get_movies))

while True:

    x = input()

    print("Chcesz obejrzeć coś? (Tak/Nie), Losowe odtwarzanie od 1 do 100 (Widownia)")
    if x == "Nie": break
    if x == "Widownia": print("Chcesz to zrobić (1) raz czy (10) razy?")
    if x == "1": print(f"Odtworzenia {widownia} {Karaiby}")
    if x == "10": print(f"Odtworzenia {widowniax10} {Karaiby}")
    if x == "Tak": print("Serial czy film")
    if x == "Film": print("Karaiby, Scooby doo, Dom strachu?")
    if x == "Karaiby": print(f"Odtworzenia {play} {Karaiby}")
    if x == "Dom strachu": print(f"Odtworzenia {play1} {Dom_strachu}")
    if x == "Scooby doo": print(f"Odtworzenia {play2} {Scooby_doo}")
    if x == "Serial": print("Spongebob, Dexter, Rodzinka?")
    if x == "Spongebob": print(f"Odtworzenia {play3} {Spongebob}")
    if x == "Dexter": print(f"Odtworzenia {play4} {Dexter}")
    if x == "Rodzinka": print(f"Odtworzenia {play5} {Rodzinka}")
