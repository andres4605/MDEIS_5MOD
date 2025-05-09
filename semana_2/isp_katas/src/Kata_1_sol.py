from abc import ABC, abstractmethod

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass

class Runnable(ABC):
    @abstractmethod
    def run(self):
        pass

class Bird(Flyable, Runnable):
    def fly(self):
        print("Pájaro volando")

    def run(self):
        print("Pájaro corriendo")

class Fish(Swimmable):
    def swim(self):
        print("Pez nadando")

class Dog(Swimmable, Runnable):
    def swim(self):
        print("Perro nadando")

    def run(self):
        print("Perro corriendo")

#el perro solo pede corres y nadar
#pirulo = Dog()
#pirulo.swim()

pirulo = Dog()
pirulo.run()

