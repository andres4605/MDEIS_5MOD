from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan(self):
        pass

class Faxable(ABC):
    @abstractmethod
    def fax(self):
        pass

class BasicPrinter(Printable):
    def print(self):
        print("Imprimiendo documento")

class MultiFunctionPrinter(Printable, Scannable, Faxable):
    def print(self):
        print("Imprimiendo documento multifunción")

    def scan(self):
        print("Escaneando documento multifunción")

    def fax(self):
        print("Enviando fax desde multifunción")
#EL DOCUEMNTO SOLO PUEDE SER IMPRIMIDO PO BASICPRINTER PERO IGUAL PUEDE SER IMPRIMIDO,ESCANEADO Y FAXEADO 
# POR MULTIFUNCTIONPRINTER
#  
# documento = BasicPrinter()
# documento.print()

documento = MultiFunctionPrinter()
documento.print()
