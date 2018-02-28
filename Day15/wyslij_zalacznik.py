import os
from poczta_zalacznik import *
from secrets import *

poczta = Poczta(moj_login, moje_haslo)

adresaci = [moj_login]
temat = "Hello from Marcin - załączniki"
tresc = "To są załączniki"

# zalaczniki = ["c:\\wyslac\\plik1.txt",
#               "c:\\wyslac\\plik2.txt",
#               "c:\\wyslac\\plik3.txt"]

root = "c:\\wyslac"

# zalaczniki = [os.path.plik.join(root, plik) for plik in os.listdir(root)]
# print(zalaczniki)

zalacz = []
for plik in os.listdir(root):
    pelna_sciezka = os.path.join(root, plik)
    zalacz.append(pelna_sciezka)

poczta.wyslij_wiadomosc(adresaci, temat, tresc, zalacz)
