import os, shutil, sys

print("Folder roboczy:",os.getcwd())

print(sys.argv)

f_roboczy = os.getcwd()

if len(sys.argv) != 3:
    print("Podaj komendę w formacie: python rename.py .jpg nowa_nazwa")
    raise SyntaxError

rozszerzenie = sys.argv[1]
nowa_nazwa = sys.argv[2]

for indeks, plik in enumerate(os.listdir(f_roboczy)):
    stary_plik = os.path.join(f_roboczy, plik)

    stara_nazwa, st_rozsz = os.path.splitext(plik)

    if st_rozsz == rozszerzenie:
        nowy_root = "{}_{}.{}".format(nowa_nazwa, indeks, rozszerzenie)
        nowy_plik = os.path.join(f_roboczy, nowy_root)

        shutil.move(stary_plik, nowy_plik)

print("Udało się")