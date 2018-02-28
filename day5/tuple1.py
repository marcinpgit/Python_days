# krotki

x = "jeden"
print(type(x))

y = "jeden",
print(type(y))

z = ("dwa", "trzy")
print(z)
print(type(z))

# tuple jest typem niemutowalnym
# z[0] = "jeden"
print()

for element in z:
    print(element)
print()
for indeks, element in enumerate(z):
    print(indeks, element)


