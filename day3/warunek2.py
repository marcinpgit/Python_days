imie = input("Podaj imię: ")
print("Witaj, ", imie)

if imie.isalpha():
    print("Hello,", imie)
    if "a" in imie:
        print("Twoje imię ma literę 'a'")
    elif "b" in imie:
        print("Twoje imię ma literę 'b'")

elif imie.isalnum():
    print("Imię musi mieć tylko litery")
elif "a" in imie:
    print("Imię zawiera literę 'a'")
