# czy liczba jest podzielna przez 3, 5 lub 7

# input
liczba = input("podaj liczbę: ")
# sprawdź czy tylko cyfry
if liczba.isdigit():
    # jeśli podzielna przez 3
    if int(liczba) % 3 == 0:
        # napisz że podzielna przez 3
        print("Liczba jest podzielna przez 3")
        # w prz. razie czy podzielna przez 5
    elif int(liczba) % 5 == 0:
        # napisz podzielna przez 5
        print("Liczba podzielna przez 5")
    elif int(liczba) % 7 == 0:
        print("Liczba jest podzielna przez 7")

#
else:
    print("Podaj liczbę!!!!!")