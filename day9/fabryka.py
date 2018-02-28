from samochod2 import *

auto1 = Samochod("Toyota", "Yaris", "Niebieska")
print(auto1.marka)
print(auto1.model)
print(auto1.kolor)

print()

print(auto1.silnik)
auto1.silnik = "1.0 90 KM"
print(auto1.silnik)

auto1.il_drzwi = 3
print(auto1.il_drzwi)

print()

auto1.jedz()
print(auto1.czy_jedzie)

print()

auto2 = Samochod("Volvo", "XC60 nowe", "Dark Grey")
print(auto2.marka)
print(auto2.model)
print(auto2.kolor)
auto2.jedz()

print()

auto1.zatrzymaj()
print(auto1.czy_jedzie)
