from zwierze import Zwierze
from czlowiek import Czlowiek
from czlowiek import Student

animal1 = Zwierze("mamut")
animal2 = Czlowiek("Janek")

print(animal1.imie)
print(animal2.imie)
print()
animal1.biega()
animal2.biega()
print()
Zwierze.biega(animal2)
print()
student1 = Student("Janek", 43354)
print(student1.nr_indeksu)
