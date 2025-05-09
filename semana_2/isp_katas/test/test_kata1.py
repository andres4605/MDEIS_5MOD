import unittest

class TestAnimalInterfaces(unittest.TestCase):
    def test_bird_can_fly(self):
        from src.Kata_1_sol import Bird
        bird = Bird()
        self.assertIsNone(bird.fly())

    def test_fish_can_swim(self):
        from src.Kata_1_sol import Fish
        fish = Fish()
        self.assertIsNone(fish.swim())

    def test_dog_can_run(self):
        from src.Kata_1_sol import Dog
        dog = Dog()
        self.assertIsNone(dog.run())

