# Kata 5: Interfaz de Dispositivo IoT
# Objetivo: Diseñar interfaces para capacidades específicas de dispositivos.

# Crear una interfaz SmartDevice con los métodos turnOn(), turnOff(), connectToWiFi() y playMusic().
# Implementar las clases SmartLight y SmartSpeaker.
# Identificar el problema: SmartLight no necesita playMusic().
# Refactorizar: Crear interfaces más pequeñas (PowerControllable, WiFiConnectable, MusicPlayable) e implementarlas selectivamente.
from abc import ABC, abstractmethod
class SmartDevice:
    def turnOn(self):
        pass

    def turnOff(self):
        pass

    def connectToWiFi(self):
        pass

    def playMusic(self):
        pass

class SmartLight(SmartDevice):
    def turnOn(self):
        print("Luz encendida")

    def turnOff(self):
        print("Luz apagada")

    def connectToWiFi(self):
        print("Luz conectada al WiFi")

    def playMusic(self):
        pass  # No aplica

class SmartSpeaker(SmartDevice):
    def playMusic(self):
        print ("Reproduce la musica")

    def turnOn(self):
        print ("Enciende el altavoz")

    def turnOff(self):
        print ("Apaga el altavoz")

    def connectToWiFi(self):
        print("Altavoz conectado al WiFi")

#la clase SmartLigth no nesecita del metodo playMusic 
# mientras que la clase SmartSpeaker nesecita de todos los metodos

Ligh =SmartLight()
Ligh.playMusic()

speaker =SmartSpeaker()
speaker.playMusic()