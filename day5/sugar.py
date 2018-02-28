lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lista2 = []

for element in lista:
    lista2.append(element*element)
    print(lista2)

print()

# to co wyżej i poniżej jest równoważne

lista3 = []

lista3 = [element**2 for element in lista]

print(lista3)

lista4 = [element**2 for element in lista if element % 3 == 0]

print(lista4)

