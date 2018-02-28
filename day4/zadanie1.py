# policzyc ilosc liczb parzystych i nieparzystych w zakresie

zakres = range(23, 8848)
ilosc_parzyste = 0
ilosc_nieparzyste = 0

for i in zakres:
    if i % 2 == 0:
        ilosc_parzyste += 1
    else:
        ilosc_nieparzyste += 1


print("Ilość parzystych: {}, nieparzystych: {}".format(ilosc_parzyste, ilosc_nieparzyste))