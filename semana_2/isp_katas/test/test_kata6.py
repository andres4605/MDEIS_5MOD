import unittest

class TestPaymentProcessors(unittest.TestCase):
    def test_credit_card_processor(self):
        from src.Kata_6_sol import CreditCardProcessor
        processor = CreditCardProcessor()
        self.assertIsNone(processor.processCreditCard(100))

    def test_paypal_processor(self):
        from src.Kata_6_sol import PayPalProcessor
        processor = PayPalProcessor()
        self.assertIsNone(processor.processPayPal(150))

    def test_crypto_processor(self):
        from src.Kata_6_sol import CryptoProcessor
        processor = CryptoProcessor()
        self.assertIsNone(processor.processCrypto(300))
