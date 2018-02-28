import os, shutil, send2trash

print(shutil.disk_usage('c:\\'))
print()

print(os.getcwd())
print()

os.chdir("c:\\")
print(os.getcwd())

# os.mkdir("pyta")

# shutil.copytree("c:\\wyslac", "c:\\pyta\\wyslac")

zawartosc = os.listdir("c:\\pyta\\wyslac")
print(zawartosc)

print()

for plik in zawartosc:
    print(plik)

print()

for folder, podfoldery, pliki in os.walk("c:\\pyta"):
    print("Obecny folder to: ", folder)

    for podfolder in podfoldery:
        print("Podfolder: {} w podfolderze {}".format(podfolder, folder))
    for plik in pliki:
        print("Plik {} w folderze {}".format(plik, folder))

    print()