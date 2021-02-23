class Pet:
    def __init__(self, name, greeting="Hello"):
        self.name = name
        self.greeting = greeting

    def say_hi(self):
        print(f"{self.greeting}, I'm {self.name}!")


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, "Meow")

    legNumber = 4

    @classmethod
    def legs_count(cls):
        print('My number of legs is:', cls.legNumber)


class Parrot(Pet):
    def __init__(self, name):
        super().__init__(name, "Squawk")

    def say_hi(self):
        print(f"{self.greeting}, my name is {self.name}!")

    legNumber = 2

    @classmethod
    def legs_count(cls):
        print('My number of legs is:', cls.legNumber)


my_pet = Pet("Gaston")
my_pet.say_hi()

cat = Cat("Félix")
cat.say_hi()
cat.legs_count()

parrot = Parrot("Coco")
parrot.say_hi()
Parrot.legs_count()

# 👇 ça c'est juste pour dire qu'on peut appeler `legs_count` directement sur
# 👇 la classe `Pet` sans avoir besoin d'une instance – `cls` est l'équivalent
# 👇 de `self`, mais pour une classe ; ça vaudra `Pet` par exemple.
# do nothing
