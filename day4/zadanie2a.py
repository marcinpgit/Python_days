import string

zdanie = input("Napisz coś: ")


litery = 0
cyfry = 0
male_litery = 0
duze_litery = 0

for znak in zdanie:
    if znak.isdigit():
        cyfry += 1
    elif znak.isalpha():
        litery += 1
        if znak in string.ascii_lowercase:
            male_litery += 1
        else:
            duze_litery += 1

print("Litery: ", litery)
print("Cyfry: ", cyfry)
print("Małe litery: ", male_litery)
print("Duże litery: ", duze_litery)