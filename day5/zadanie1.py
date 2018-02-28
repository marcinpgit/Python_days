# program usuwający duplikaty z listy

lista = [10, 20, 30, 40, 20, 45, 54, 45, 90, 90, 101]
lista_bez_duplikatów = []

for num in lista:
    if num not in lista_bez_duplikatów:
        lista_bez_duplikatów.append(num)
print(lista_bez_duplikatów)



