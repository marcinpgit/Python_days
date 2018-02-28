# dict
# slowniki nie są upożątkowane

slownik = {}
print(slownik)
print(type(slownik))
print()
slownik2 = {'imie':'Adam', 'nazwisko':'Kowalski', 1:"jedynka"}
slownik3 = {("jeden", "dwa"):[1,2,3,4,5,56]}
lista_slownikow = [{"nazwisko":"Kowalski"}, {}]
slownik5 = {3435:{"klucz wew":"wartość wew"}}
print(slownik5[3435])
print(slownik2)
print(len(slownik2))
print(slownik2[1])  # to nie jest indeks tylko klucz!!!!!!!!!
print(slownik3[("jeden", "dwa")])
print(slownik2.keys())
print(slownik2.values())
print(slownik2.items())

print()

slownik2['wiek'] = 32
print(slownik2)
del slownik2['wiek']
print(slownik2)


