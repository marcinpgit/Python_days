from zwierze import Zwierze

class Czlowiek(Zwierze):
    def __init__(self, imie):
        Zwierze.__init__(self, imie)

# jak nie zdefiniuję def biega to odwoła się do pliku zwierze (tam jest ta metoda)
    def biega(self):
        print("Człowiek {} biega".format(self.imie))

class Student(Czlowiek):
    def __init__(self, imie, indeks):
        # super oznacza że bezpośredni rodzic
        super().__init__(imie)
        self.nr_indeksu = indeks