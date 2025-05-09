from abc import ABC, abstractmethod

class Drivable(ABC):
    @abstractmethod
    def drive(self):
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Sailable(ABC):
    @abstractmethod
    def sail(self):
        pass

class Car(Drivable):
    def drive(self):
        print("Conduciendo auto")

class Plane(Flyable):
    def fly(self):
        print("Volando avión")

class Boat(Sailable):
    def sail(self):
        print("Navegando bote")

#Solo permite usar las funciones implementadas funcionales
peta = Car()
peta.drive

peta = Plane()
peta.fly()

peta = Boat()
peta.sail()