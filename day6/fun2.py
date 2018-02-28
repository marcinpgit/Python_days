# definiowanie z argumentami

def drukuj_kwadraty():
    liczby = range(12)
    for l in liczby:
        print(l**2)

drukuj_kwadraty()

print()

def drukuj_kwadraty(max_num):
    for l in range(max_num):
        print(l**2)

drukuj_kwadraty(10)
drukuj_kwadraty(100)