# zmień stringa w listę wyrazów (przecinki usuwamy)

zdanie = "Ala ma kota, kot ma Ale"
zdanie = zdanie.replace(',', '')
lista = zdanie.split()
print(lista)
print(zdanie)

