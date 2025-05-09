# Kata 4: Gestión de Sensores en un Sistema de Monitoreo
# Objetivo: Diseñar interfaces específicas para diferentes tipos de sensores.

# Crear una interfaz Sensor con los métodos readTemperature(), readPressure() y readHumidity().
# Implementar las clases TemperatureSensor, PressureSensor y HumiditySensor.
# Identificar el problema: Cada sensor implementa métodos que no necesita.
# Refactorizar: Dividir Sensor en interfaces más pequeñas (TemperatureReadable, PressureReadable, HumidityReadable) e implementar solo las relevantes en cada clase.
from abc import ABC, abstractmethod
class Sensor:
    def readTemperature(self):
        pass

    def readPressure(self):
        pass

    def readHumidity(self):
        pass

class TemperatureSensor(Sensor):
    def readTemperature(self):
        print("Temperatura: 25°C")

    def readPressure(self):
        pass  # No aplica

    def readHumidity(self):
        pass  # No aplica

class PressureSensor(Sensor):
    def readTemperature(self):
        pass  # No aplica

    def readPressure(self):
        print ("Presion: 1013.25 mbar")

    def readHumidity(self):
        pass # No aplica

class HumiditySensor(Sensor):
    def readTemperature(self):
        pass  # No aplica

    def readPressure(self):
        pass # No aplica

    def readHumidity(self):
       print ("Humedad: 25 g/m3")


# cada clase de sensor tiene metodos que no se usan
ambiente = HumiditySensor()
ambiente.readPressure

ambiente = PressureSensor()
ambiente.readTemperature

ambiente = TemperatureSensor()
ambiente.readHumidity
