from pracownik import Pracownik

prac1 = Pracownik("Jan", "Kowalski")
prac1.wypisz_imie()
print()

print(prac1.stanowisko) # property wywolujemy jak zmienna bez () pomimo def

print()

prac1.stanowisko = "mechanik"
print(prac1.stanowisko)
print()

prac1.pensja = 6000
print("Mechanik zarabia {}".format(prac1.pensja))


