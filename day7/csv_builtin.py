import csv

# odczytamy csv
with open('osoby.txt', 'r') as plik:
    # tworzymy czytnik
    czytnik = csv.reader(plik)

    for line in czytnik:
        print(line)

dane = ["Bartosz", "Mojo", 33]

with open('osoby.txt', 'a') as plik:
    # tworzymy zapisywacz
    zapisywacz = csv.writer(plik)
    zapisywacz.writerow(dane)
