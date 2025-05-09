from abc import ABC, abstractmethod

class TemperatureReadable(ABC):
    @abstractmethod
    def readTemperature(self):
        pass

class PressureReadable(ABC):
    @abstractmethod
    def readPressure(self):
        pass

class HumidityReadable(ABC):
    @abstractmethod
    def readHumidity(self):
        pass

class TemperatureSensor(TemperatureReadable):
    def readTemperature(self):
        print("Temperatura: 25°C")

class PressureSensor(PressureReadable):
    def readPressure(self):
        print("Presión: 1013 hPa")

class HumiditySensor(HumidityReadable):
    def readHumidity(self):
        print("Humedad: 60%")

# cada clase sensor solo tiene los metodos que son necesarios
ambiente = HumiditySensor()
ambiente.readHumidity

ambiente = PressureSensor()
ambiente.readPressure

ambiente = TemperatureSensor()
ambiente.readTemperature