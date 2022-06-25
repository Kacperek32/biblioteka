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
