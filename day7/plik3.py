plik = open('mojplik.txt')

print("To jest wydrukowana pierwsza linijka:")

print(plik.readline(), end = '')

tresc = plik.read(16)
print(tresc)

plik.close()
