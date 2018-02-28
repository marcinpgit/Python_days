# metody specjalne

from ogloszenia import Ogloszenie

o1 = Ogloszenie(2000, miejscowosc="Sopot")
o2 = Ogloszenie(3000, miejscowosc="Gdańsk")

print(o1)
print(o2)

suma = o1 + o2

print()

print("Suma wynosi: ", suma)

# jak zakomentuję del poniżej to też pokaże co na koniec pousuwał bo w pliku
# ogloszenie.py zainicjalizowałem __del__, bez inicjalizacji pousuwa bez pokazywania
del o1
print("Obiekt o1 usunąłem.")
print(o2.cena)
print()
# !!!!!!!!!!!!
# usunął również o2 bo zakończył się program i wszystkie obiekty pousuwał aby zwolnić pamięć


