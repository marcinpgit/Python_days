def kwadrat(liczba):
    """Zwraca kwadrat podanej liczby"""
    return liczba**2

def pole_prostokata(bok_a, bok_b):
    """Zwraca pole prostokąta"""
    if bok_a == bok_b:
        return kwadrat(bok_a)
    else:
        return bok_a * bok_b

print(pole_prostokata(5, 4))
print(pole_prostokata(5, 5))
