import requests

# odpowiedz = requests.get("http://trojmiasto.pl/")
# print(odpowiedz.status_code)
# print()

obrazek = "http://static1.s-trojmiasto.pl/zdj/c/n/9/1829/871x0/1829690-Na-osiedlu-Cyganska-Gora-czesc-z-mieszkancow-wykupila-mieszkania-z-90-proc-bonifikata-Pozostali-decyzja-radnych-wykupia-z-bonifikata-nie-wieksza-niz-35-proc.jpg"

odpowiedz = requests.get(obrazek)
print(odpowiedz.status_code)
print()
bajty = 0
with open("pliczek.jpg", "wb") as plik:
    for kawalek in odpowiedz.iter_content(100000):
        ilosc = plik.write(kawalek)
        bajty += ilosc

print(bajty)