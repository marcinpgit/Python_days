class Osoba(object):
    """Definiuje informacje o osobach"""

    def __init__(self, imie, nazwisko, pesel):
        """Inicjalizuję instancję klasy osoba"""
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = None
        self.plec = None

        if len(str(pesel)) == 11:
            self.pesel = pesel
        else:
            print("Pesel musi mieć 11 znaków")
            self.pesel = None


    def wypisz(self):
        print(self.imie, self.nazwisko)

    def spr_pesel(self):
        if len(str(self.pesel)) == 11:
            return True
        return False
