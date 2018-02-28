# hasło musi mieć min 6 znaków, litery i cyfry muszą się w nim znajdować

# login = input("Podaj login: ")

haslo = input("Podaj hasło: ")

while len(haslo) < 6:
    print ("Hasło jest za krótkie!", end = " ")
    print("Podaj prawidłowe hasło")
    haslo = input("Podaj prawidlowe haslo: ")

while not haslo.isalnum():
    print("Hasło musi mieć litery i cyfry!")
    haslo = input("Podaj odpowiednie hasło: ")

print("Podano prawidłowe hasło.")