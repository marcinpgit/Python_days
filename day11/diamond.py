class Animal(object):
    def __init__(self, imie):
        self.name = imie

    def say(self):
        print("Zwierzak {} nie mówi".format(self.name))

    def capitalize_name(self):
        self.name = str(self.name).capitalize()

class Horse(Animal):
    def __init__(self, imie):
        super().__init__(imie)

    def say(self):
        print("{} rży!".format(self.name))

    def jump(self):
        print("Koń {} skacze!".format(self.name))

class Donkey(Animal):
    def __init__(self, imie):
        super().__init__(imie)

    def say(self):
        print("iihihihihihihhahaha jestem osioł!!")

    def run(self):
        print("Jestem uparty, ja nie biegam!")

# Donkey na pierwszym miejscu to Mule dziedziczy z Donkey
class Mule(Donkey, Horse):

    def say(self):
        print("Muł mówi coś takiego:", end="")
        super().say()
        Donkey.say(self)

mul = Mule("muł edek")
mul.capitalize_name()
mul.say()
mul.run()
mul.jump()

print()
osiol = Donkey("antoni")
osiol.capitalize_name()
osiol.say()
osiol.run()

print()
kon = Horse("gniady")
kon.capitalize_name()
kon.say()
kon.jump()

print()
zwierz = Animal("ciasteczkowy potwór")
zwierz.capitalize_name()
zwierz.say()

