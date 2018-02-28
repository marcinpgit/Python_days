from samochod3 import Samochod
from silnik import *

t8 = Silnik(2000, 400, "Benzyna + prąd")
print(t8.paliwo)

volvo = Samochod("Volvo", "XC 60", t8)
print("{} {} ma silnik {}".format(volvo.marka, volvo.model, volvo.silnik.V))
print()
print("Silnik Volvo pracuje na: ", volvo.silnik.paliwo)

# print(volvo)
print()

bmw = Samochod("BMW", "3", None)

silnik_bmw = Silnik(3000, 180, "Diesel")
bmw.silnik = silnik_bmw

print("Silnik BMW ma moc: ", bmw.silnik.moc_KM)


