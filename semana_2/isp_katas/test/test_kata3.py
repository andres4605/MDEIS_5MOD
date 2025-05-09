import unittest

class TestVehicleInterfaces(unittest.TestCase):
    def test_car_can_drive(self):
        from src.Kata_3_sol import Car
        car = Car()
        self.assertIsNone(car.drive())

    def test_plane_can_fly(self):
        from src.Kata_3_sol import Plane
        plane = Plane()
        self.assertIsNone(plane.fly())

    def test_boat_can_sail(self):
        from src.Kata_3_sol import Boat # type: ignore
        boat = Boat()
        self.assertIsNone(boat.sail())
