# Python provides an Absctract Base Class in abc
from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta):
    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):
    def do_say(self):
        print('woof')
class Cat(Animal):
    def do_say(self):
        print('meaow')
class Bat(Animal):
    def do_say(self):
        print('------')

# declare a factory method
class CreatureFactory():
    def make_sound(self, object_type):
        return eval(object_type)().do_say()

if __name__ == '__main__':
    cf = CreatureFactory()
    # ask the user which creature
    animal = input('which creature? ')
    cf.make_sound(animal)