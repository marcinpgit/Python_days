plik = open('mojplik.txt', "r")

linijka = plik.readline()
print(len(linijka))

# sprawdzam pozycje kursora po instrukcji readline()
print(plik.tell())

linijka = plik.readline()
print(linijka)

print(plik.tell())

plik.close()