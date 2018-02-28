zdanie = input("Napisz coś: ")
samogloski = 'aeiouyAEIOUY'
litery = 0
cyfry = 0
ilosc_samoglosek = 0
ilosc_spolglosek = 0

for znak in zdanie:
    if znak.isdigit():
        cyfry += 1
    elif znak.isalpha():
        litery += 1
        if znak in samogloski:
            ilosc_samoglosek += 1
        else:
            ilosc_spolglosek += 1

print("Litery: ", litery)
print("Cyfry: ", cyfry)
print("Samogłoski: ", ilosc_samoglosek)
print("Spółgłoski: ", ilosc_spolglosek)