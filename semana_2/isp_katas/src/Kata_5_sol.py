from abc import ABC, abstractmethod

class PowerControllable(ABC):
    @abstractmethod
    def turnOn(self):
        pass

    @abstractmethod
    def turnOff(self):
        pass

class WiFiConnectable(ABC):
    @abstractmethod
    def connectToWiFi(self):
        pass

class MusicPlayable(ABC):
    @abstractmethod
    def playMusic(self):
        pass

class SmartLight(PowerControllable, WiFiConnectable):
    def turnOn(self):
        print("Luz encendida")

    def turnOff(self):
        print("Luz apagada")

    def connectToWiFi(self):
        print("Luz conectada al WiFi")

class SmartSpeaker(PowerControllable, WiFiConnectable, MusicPlayable):
    def turnOn(self):
        print("Altavoz encendido")

    def turnOff(self):
        print("Altavoz apagado")

    def connectToWiFi(self):
        print("Altavoz conectado al WiFi")

    def playMusic(self):
        print("Reproduciendo música")

#cada clase implementa los metodos que usa
light = SmartLight()
light.connectToWiFi()

speaker = SmartSpeaker()
speaker.playMusic()


