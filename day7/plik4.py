plik = open("mojplik.txt", "r")

linijki = plik.readlines()

print(linijki)

print()

for linijka in linijki:
    print(linijka, end = '')

plik.close()