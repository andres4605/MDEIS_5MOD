## Kata 1: Interfaz Monolítica - Violando y Corrigiendo ISP
#Objetivo: Crear una interfaz monolítica que viole ISP.
#Crear una interfaz Animal con los métodos fly, swim y run().
#Implementar las clases Bird, Fish y Dog utilizando la interfaz Animal.
#Identificar el problema: No todos los animales pueden realizar todas las acciones.
#Refactorizar: Dividir Animal en interfaces más pequeñas (Flyable, Swimmable, Runnable) e implementar solo las relevantes en cada clase.
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def run(self):
        pass

class Bird(Animal):
    def fly(self):
        print("Pájaro volando")

    def swim(self):
        pass  # No nada

    def run(self):
        print("Pájaro corriendo")

class Fish(Animal):
    def fly(self):
        pass  # No vuela

    def swim(self):
        print("Pez nadando")

    def run(self):
        pass  # No corre

class Dog(Animal):
    def fly(self):
        pass  # No vuela

    def swim(self):
        print("Perro nadando")

    def run(self):
        print("Perro corriendo")

## ERROR perro no vuela
pirulo = Dog()
pirulo.fly()

## perro si corre
pirulo = Dog()
pirulo.run()