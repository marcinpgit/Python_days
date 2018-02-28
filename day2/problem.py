# system binarny nie jest w stanie pokazać dzisiętnych - uwaga na float
w = 0.1 + 0.1 + 0.1 == 0.3

print (w)
print ("{:.20f}".format(0.3))

# to jest zaokrąglanie liczby float!
z = round (0.1 + 0.1 + 0.1, 10) == round(0.3, 10)
print (z)



