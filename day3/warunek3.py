imie = input("Podajh imię: ")

if "a" in imie:
    print("Litera 'a' jest w imieniu")
elif "A" in imie:
    print("Litera 'A' jest w imieniu")
else:
    print("W imieniu nie ma literek 'a' oraz 'A'")

if imie.endswith("a"):
    print("Chyba jesteś kobietą")
else:
    print("Chyba jesteś mężczyzną")

