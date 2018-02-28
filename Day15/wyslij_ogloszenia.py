from ogloszenie import Ogloszenie
import secrets
from wyslij_zalacznik import *
from poczta_zalacznik import Poczta

Ogloszenie.wczytaj_ogloszenie("ogloszenia.dat")

ads = Ogloszenie.ogloszenia
tekst = ""

for ad in ads:
    tekst += ad.opis + ad.link
    tekst += "---------------\n"

print(tekst)

# tu wysyłamy tekst wiadomości z ogłoszenia
mailer.Poczta(moj_login, moje_haslo)
mailer.wyslij_wiadomosc([moj_login], "ogloszenia", tekst)

# SPRAWDZIĆ CZEMU MAILER NIE DZIAŁA

