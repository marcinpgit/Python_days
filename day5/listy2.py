lista = [1, "dwa", "trzy", 4]
for element in lista:
    print(element)

print()

lista_z = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for element in lista_z:
    print(element, type(element))
    for subelement in element:
        print(subelement, type(subelement))
        print(subelement)

print()

print(lista[1:3])

print()

print(lista)
x = lista.pop()
print(x)
print(lista)