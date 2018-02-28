lista = ["kwiatek", "woda", "doniczka", "ziemia"]

el_to_remove = "kwiatek"

lista.remove(el_to_remove)
print(lista)

if el_to_remove in lista:
    lista.reverse(el_to_remove)
    print(lista)