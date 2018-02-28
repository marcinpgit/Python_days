class Samochod(object):

    def __init__(self, marka, model, kolor):
        self.marka = marka
        self.model = model
        self.kolor = kolor
        self.czy_jedzie = None
        self.silnik = None

    def jedz(self):
        print(self.marka, ": Jadę")
        self.czy_jedzie = True

    def zatrzymaj(self):
        self.czy_jedzie = False



