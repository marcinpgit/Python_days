try:
    with open('dane.txt') as plik:
        print(plik.read())
except FileNotFoundError as e:
    print(e.args)
    print("Podany plik nie istnieje")
    raise ValueError("Komunikat mój o błędzie")
except Exception:
    print("Pojawił się błąd!!")

print()
print("Dalsza część programu.")