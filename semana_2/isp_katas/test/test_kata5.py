import unittest

class TestSmartDevices(unittest.TestCase):
    def test_smart_light(self):
        from src.Kata_5_sol import SmartLight
        light = SmartLight()
        self.assertIsNone(light.turnOn())
        self.assertIsNone(light.turnOff())
        self.assertIsNone(light.connectToWiFi())

    def test_smart_speaker(self):
        from src.Kata_5_sol import SmartSpeaker
        speaker = SmartSpeaker()
        self.assertIsNone(speaker.turnOn())
        self.assertIsNone(speaker.turnOff())
        self.assertIsNone(speaker.connectToWiFi())
        self.assertIsNone(speaker.playMusic())
