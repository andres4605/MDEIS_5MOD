import unittest

class TestSensorInterfaces(unittest.TestCase):
    def test_temperature_sensor(self):
        from src.Kata_4_sol import TemperatureSensor
        sensor = TemperatureSensor()
        self.assertIsNone(sensor.readTemperature())

    def test_pressure_sensor(self):
        from src.Kata_4_sol import PressureSensor
        sensor = PressureSensor()
        self.assertIsNone(sensor.readPressure())

    def test_humidity_sensor(self):
        from src.Kata_4_sol import HumiditySensor
        sensor = HumiditySensor()
        self.assertIsNone(sensor.readHumidity())
