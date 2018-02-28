import requests

obrazek = "http://static1.s-trojmiasto.pl/zdj/c/n/9/1829/871x0/1829690-Na-osiedlu-Cyganska-Gora-czesc-z-mieszkancow-wykupila-mieszkania-z-90-proc-bonifikata-Pozostali-decyzja-radnych-wykupia-z-bonifikata-nie-wieksza-niz-35-proc.jpg"

def pobierz_foto(link, lokalizacja):
    """link - adres obrazka w sieci
    lokalizacja - zcieżka dysku"""

    odpowiedz = requests.get(link)

    if odpowiedz.status_code == 200:
        bajty = 0
        try:
            with open(lokalizacja, "wb") as plik:
                for kawalek in odpowiedz.iter_content(100000):
                    ilosc = plik.write(kawalek)
                    bajty += ilosc
        except FileNotFoundError:
            print("tworze folder i zapisuje plik")
            bajty = 23423

        print(bajty)