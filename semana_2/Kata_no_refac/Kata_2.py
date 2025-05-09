# Kata 2: Sistema Legacy con Métodos No Utilizados
# Objetivo: Identificar métodos no utilizados en un sistema legacy.

# Crear una interfaz LegacyPrinter con los métodos print(), scan() y fax().
# Implementar una clase BasicPrinter que solo utilice print().
# Identificar el problema: BasicPrinter se ve obligada a implementar métodos no utilizados.
# Refactorizar: Dividir LegacyPrinter en Printable, Scannable y Faxable.

from abc import ABC, abstractmethod

class LegacyPrinter(ABC):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def scan(self):
        pass

    @abstractmethod
    def fax(self):
        pass

class BasicPrinter(LegacyPrinter):
    def print(self):
        print("Imprimiendo documento")

    def scan(self):
        pass  # No soporta escaneo

    def fax(self):
        pass  # No soporta fax

documento = BasicPrinter()
documento.print()

# documento = BasicPrinter()
# documento.scan()

