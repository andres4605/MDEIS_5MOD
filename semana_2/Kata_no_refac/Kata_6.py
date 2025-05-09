# Kata 6: Sistema de Pago en E-Commerce
# Objetivo: Evitar que las clases implementen métodos irrelevantes.

# Crear una interfaz PaymentProcessor con los métodos processCreditCard(), processPayPal() y processCrypto().
# Implementar las clases CreditCardProcessor, PayPalProcessor y CryptoProcessor.
# Identificar el problema: Cada clase implementa métodos que no utiliza.
# Refactorizar: Dividir PaymentProcessor en CreditCardPayment, PayPalPayment y CryptoPayment.

from abc import ABC, abstractmethod
class PaymentProcessor:
    def processCreditCard(self, amount):
        pass

    def processPayPal(self, amount):
        pass

    def processCrypto(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def processCreditCard(self, amount):
        print(f"Pagando {amount} con tarjeta")

    def processPayPal(self, amount):
        pass  # No aplica

    def processCrypto(self, amount):
        pass  # No aplica

class PayPalProcessor(PaymentProcessor):
    def processCreditCard(self, amount):
       pass  # No aplica

    def processPayPal(self, amount):
        print(f"Pagando {amount} con PayPal")
        
    def processCrypto(self, amount):
        pass  # No aplica

class CryptoProcessor(PaymentProcessor):
    def processCreditCard(self, amount):
       pass  # No aplica

    def processPayPal(self, amount):
         pass  # No aplica
        

    def processCrypto(self, amount):
        print(f"Pagando {amount} con Cryptos")

# cada clase implenta metodos que no usa
pago = CreditCardProcessor()
pago.processCrypto(100.00)

pago = PayPalProcessor()
pago.processCreditCard(55.50)

pago = CryptoProcessor()
pago.processPayPal(0.005)