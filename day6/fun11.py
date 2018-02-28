def czy_w_zakresie(liczba, zakres):
    """Sprawdza czy podana liczba jest w zakresie. Zwraca True jeśli jest.
    (liczba) -> bool
    """
    if liczba in zakres:
        return True
    else:
        return False

x = 23
y = range(1, 23)
wynik = czy_w_zakresie(x, y)
print(wynik)

print()

liczby = [23, 345, 22456, 343, 4345, 45, 45]

for liczba in liczby:
    print(czy_w_zakresie(liczba, range(10000)))