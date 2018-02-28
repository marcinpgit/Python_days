# listy
# deklarowanie

lista = ["trzy", "jeden"]
lista1 = [2, 3, 4, 9, 0 ,3, 4]
print(lista1)
print(type(lista1))

lista2 = list("kwiatek")
print(lista2)

el_string = ''.join(lista2)
print(el_string)

lista3 = [1, "dwa", 3.0, range(3), [0, 1]]
print(lista3)
print (len(lista3))
print()

print(lista3[2])
print(lista3[4][0])

# imie = "Ala"
# imie[0] = "o"
# # stringi są imutable
# print(imie)

lista3[1] = "osiem"
print(lista3)
