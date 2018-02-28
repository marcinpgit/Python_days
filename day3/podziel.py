# czy liczba jest podzielna przez 3, 5 lub 7

# input
liczba = input("podaj liczbę: ")
podzielnik = input("podaj podzielnik ")
# sprawdź czy tylko cyfry
if liczba.isdigit() and podzielnik.isdigit():
    # jeśli podzielna przez 3
    if int(liczba) % int(podzielnik) == 0:
        # napisz że podzielna przez 3
        print("Liczba jest podzielna przez ", podzielnik)
        # w prz. razie czy podzielna przez 5
    else:
        print("Liczba nie jest podzielna")
        print("Wynik dzielenia: ", int(liczba) / int(podzielnik))
else:
    print("Podaj liczbę!!!!!")