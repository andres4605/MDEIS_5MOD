#Kata 3: Operaciones No Soportadas
# Objetivo: Manejar operaciones no soportadas.

# Crear una interfaz Vehicle con los métodos drive, fly y sail.
# Implementar las clases Car, Plane y Boat. Lanzar UnsupportedOperationException para los métodos no soportados.
# Identificar el problema: Lanzar excepciones viola ISP.
# Refactorizar: Crear interfaces separadas (Drivable, Flyable, Sailable) e implementarlas adecuadamente.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def sail(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Conduciendo auto")

    def fly(self):
        raise NotImplementedError("Un auto no puede volar")

    def sail(self):
        raise NotImplementedError("Un auto no puede navegar")

class Plane(Vehicle):
    def drive(self):
        raise NotImplementedError("Un avión no puede conducir")

    def fly(self):
        print("Volando avión")

    def sail(self):
        raise NotImplementedError("Un avión no puede navegar")

class Boat(Vehicle):
    def drive(self):
        raise NotImplementedError("Un bote no puede conducir")

    def fly(self):
        raise NotImplementedError("Un bote no puede volar")

    def sail(self):
        print("Navegando bote")


#lanza excepciones (error) haciendo referecnia que esa clase a un no es funcionañ
peta = Car()
peta.fly

peta = Plane()
peta.sail()

peta = Boat()
peta.drive()