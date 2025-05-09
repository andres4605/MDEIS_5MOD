from abc import ABC, abstractmethod

class CreditCardPayment(ABC):
    @abstractmethod
    def processCreditCard(self, amount):
        pass

class PayPalPayment(ABC):
    @abstractmethod
    def processPayPal(self, amount):
        pass

class CryptoPayment(ABC):
    @abstractmethod
    def processCrypto(self, amount):
        pass

class CreditCardProcessor(CreditCardPayment):
    def processCreditCard(self, amount):
        print(f"Pagando {amount} con tarjeta")

class PayPalProcessor(PayPalPayment):
    def processPayPal(self, amount):
        print(f"Pagando {amount} con PayPal")

class CryptoProcessor(CryptoPayment):
    def processCrypto(self, amount):
        print(f"Pagando {amount} con criptomonedas")

#cada clase implementa los metodos que usa
pago = CreditCardProcessor()
pago.processCreditCard(100.00)

pago = PayPalProcessor()
pago.processPayPal(55.50)

pago = CryptoProcessor()
pago.processCrypto(0.005)