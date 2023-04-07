from unittest import TestCase
from project.truck_driver import TruckDriver

class TestTruckDriver(TestCase):

    def setUp(self) -> None:
        self.driver = TruckDriver("Pesho", 5)
        self.cargo = {
            "Cargo1": 10
        }

    def test_valid_init(self):
        self.assertEqual("Pesho", self.driver.name)
        self.assertEqual(5, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_unsuccessful_earned_money_set_raises_error(self):
        with self.assertRaises(ValueError) as err:
            self.driver.earned_money = -1
        self.assertEqual("Pesho went bankrupt.", str(err.exception))

    def test_successful_earned_money(self):
        self.assertEqual(0, self.driver.earned_money)
        self.driver.earned_money = 1
        self.assertEqual(1, self.driver.earned_money)

    def test_add_already_added_cargo_raises_error(self):
        self.driver.available_cargos = self.cargo

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Cargo1", 10)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_successful_cargo(self):
        self.driver.available_cargos = self.cargo
        result = self.driver.add_cargo_offer("Cargo2", 3)
        self.assertEqual({"Cargo1": 10, "Cargo2": 3}, self.driver.available_cargos)
        self.assertEqual("Cargo for 3 to Cargo2 was added as an offer.", result)

    def test_drive_best_cargo_no_offer_available_raises_error(self):
        self.assertNotEquals({}, self.cargo)

        with self.assertRaises(ValueError) as err:
            self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", str(err.exception))

    def test_drive_best_cargo_offer(self):
        self.driver.add_cargo_offer("Location1", 300)
        self.driver.add_cargo_offer("Location2", 400)

        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("Pesho is driving 400 to Location2.", result)

    def test_eat(self):
        self.driver.earned_money = 40
        self.driver.eat(250)
        self.assertEqual(20, self.driver.earned_money)

    def test_sleep(self):
        self.driver.earned_money = 50
        self.driver.sleep(1000)
        self.assertEqual(5, self.driver.earned_money)

    def test_pump_gas(self):
        self.driver.earned_money = 1000
        self.driver.pump_gas(1500)
        self.assertEqual(500, self.driver.earned_money)

    def test_repair_truck(self):
        self.driver.earned_money = 8000
        self.driver.repair_truck(10000)
        self.assertEqual(500, self.driver.earned_money)

    def test__repr(self):
        result = self.driver
        self.assertEqual('Pesho has 0 miles behind his back.', str(result))