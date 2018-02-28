class Zawodnik(object):

    def __init__(self, imie, dyscyplina):
        self.name = imie
        self.dyscyplina = dyscyplina
        self.__numer_koszulki = None

    @staticmethod
    def __sprawdz_numer(numer):
        """Ma sprawdzać czy numer koszulki jest poprawny"""
        if numer < 0 or numer > 99:
            return False
        else:
            return True

    def zmien_numer(self, nowy_numer):
        if not Zawodnik.__sprawdz_numer(nowy_numer):
            print("Niewłaściwy numer.")
        else:
            self.__numer_koszulki = nowy_numer

    def daj_numer_koszulki(self):
        return self.__numer_koszulki


koszykarz = Zawodnik("Michael Jordan", "Koszykówka")
koszykarz.zmien_numer(23)
print(koszykarz.name, koszykarz.daj_numer_koszulki())
print()

koszykarz.__Zawodnik__numer_koszulki = 45
print(koszykarz.daj_numer_koszulki())
print()

pilkarz = Zawodnik("Robert Lewandowski", "Nożna")
pilkarz.zmien_numer(123)
print(pilkarz.__dict__)
print()
pilkarz.numer_koszulki = 234
print(pilkarz.__dict__)
print(pilkarz.name, pilkarz.numer_koszulki)
print()

print(Zawodnik.__dict__)
print()
print(koszykarz.__dict__)
