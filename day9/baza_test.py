from osoba import *

baza = []

os1 = Osoba('Adam', 'Kowalski', 230945545)

os1.wypisz()
print(os1.pesel)

os2 = Osoba("Jan", "Matejko", 548798566)
os3 = Osoba("Janina", "Nowak", 548798546)

os2.wypisz()
os3.wypisz()
print(os1.spr_pesel())

baza.append(os1)
baza.append(os2)
baza.append(os3)

print(baza)

for o in baza:
    print(o.imie)