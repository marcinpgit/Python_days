# mozemy miec kilka argumentow wymaganych i domyslnych

def wypisz_dane(imie, nazwisko, kurs="Python", ilosc_dni=15):
    print(imie, nazwisko, kurs, ilosc_dni)

wypisz_dane("Marcin", "p")
wypisz_dane("Ola", "Kowalska", "Java")

wypisz_dane("Monika", "Marcin", ilosc_dni=30)
wypisz_dane("Wiktoria", "Kowalska", "JavaScript", 20)

wypisz_dane(ilosc_dni=34, imie="Wiktoria", kurs="JS", nazwisko="Kowalska")

