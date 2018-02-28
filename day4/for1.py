# pętla for

# range

x = range(100)
print(x)

for liczba in x:
    print(liczba * liczba)
print()

for litera in "Aleksandra":
    print(litera)
print()

for litera in "Aleksandra"[::-1]:
    print(litera)
print()

for litera in "Aleksandra":
    print(litera.capitalize())
print()

for litera in "Aleksandra":
    print("Nie korzystam z litery!")


imie2 = "Hermenegilda"
indeks = 0

for c in imie2:
    print(c, [indeks])
    indeks += 1

print()
imie2 = "Hermenegilda"
for i, c in enumerate(imie2):
    print(i, c)