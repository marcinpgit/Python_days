# input
liczba = input("podaj liczbę: ")
podzielnik = input("podaj podzielnik ")
# sprawdź czy tylko cyfry
if liczba.isdigit() and podzielnik.isdigit():
    wynik = int(liczba) / int(podzielnik)
    print(wynik)
    if float(round(wynik, 2)).is_integer():
        print("Liczba {0} jest podzielna przez {1}".format(liczba, podzielnik))
    else:
        print("Liczba {} nie jest podzielna przez {}".format(liczba, podzielnik))
        print("Wynik dzielenia: {:.2f}".format(wynik))
else:
    print("Podaj liczbę")