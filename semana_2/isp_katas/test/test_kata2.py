import unittest

class TestPrinterInterfaces(unittest.TestCase):
    def test_basic_printer_can_print(self):
        from src.Kata_2_sol import BasicPrinter
        printer = BasicPrinter()
        self.assertIsNone(printer.print())

    def test_advanced_printer_can_do_all(self):
        from src.Kata_2_sol import MultiFunctionPrinter
        printer = MultiFunctionPrinter()
        self.assertIsNone(printer.print())
        self.assertIsNone(printer.scan())
        self.assertIsNone(printer.fax())
