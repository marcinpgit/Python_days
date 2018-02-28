# zmienne lokalne i zmienne globalne

imie = "Ola"

def duza_litera(imie = "monika"):
    imie = imie.capitalize()
    return imie

print(duza_litera())
print(imie)