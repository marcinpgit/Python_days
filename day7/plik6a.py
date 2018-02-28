with open("mojplik.txt", "r+") as plik:
    zawartosc = plik.read()

    if zawartosc[-1] == '\n':
        # print("jest w nowej linii")
        plik.write("Dane zapisane do pliku.")
    else:
        # print("nie ma nowej linii")
        plik.write("\nDane zapisane do pliku.")
