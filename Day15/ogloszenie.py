class Ogloszenie(object):

    ogloszenia = []

    def __init__(self, opis, link):
        self.opis = self.__formatuj_opis(opis)
        self.link = link
        Ogloszenie.ogloszenia.append(self)

    def __formatuj_opis(self, opis):
        o = str(opis).split('\n')
        return ' '.join(o).strip()

    @classmethod
    def zapisz_ogloszenie(cls, nazwa_pliku):
        import pickle
        with open(nazwa_pliku, 'wb') as plik:
            pickle._dump(cls.ogloszenia, plik)

    @classmethod
    def wczytaj_ogloszenie(cls, nazwa_pliku):
        import pickle
        with open(nazwa_pliku, 'rb') as plik:
            cls.ogloszenia = pickle.load(plik, encoding='utf-8')

    def __str__(self):
        return "{} : {}".format(self.opis, self.link)


