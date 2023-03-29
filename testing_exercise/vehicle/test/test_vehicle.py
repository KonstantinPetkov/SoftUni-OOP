import unittest
from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(20.5, 175.5)

    def test_default_fuel_consumption_valid(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_valid_initializing(self):
        self.assertEqual(20.5, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(175.5, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.fuel_consumption, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_car_without_enough_fuel(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as context:
            self.vehicle.drive(100)
        self.assertEqual(str(context.exception), "Not enough fuel")

    def test_drive_car_with_enough_fuel_expect_decrease_fuel(self):
        self.vehicle.drive(2)
        self.assertEqual(18, self.vehicle.fuel)

    def test_refuel_car(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(5)
        self.assertEqual(str(context.exception), "Too much fuel")

    def test_refuel_valid(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(2)
        self.assertEqual(self.vehicle.fuel, 2)

    def test_valid__str__(self):
        self.assertEqual(str(self.vehicle), "The vehicle has 175.5 " +
                                                 "horse power with 20.5 fuel left and 1.25 fuel consumption")


if __name__ == '__main__':
    unittest.main()