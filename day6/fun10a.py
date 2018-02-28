def dodaj_imie(imie, imiona = None):
    if imiona is None:
        imiona = []
    imiona.append(imie)
    return imiona

lista1 = dodaj_imie("Ola")
lista2 = dodaj_imie("Ala")
lista3 = dodaj_imie("Piotrek")

print(lista1)
print(lista2)
print(lista3)

dodaj_imie("Piotrek", lista1)
print(lista1)