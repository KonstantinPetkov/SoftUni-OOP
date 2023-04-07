from unittest import TestCase, main
from project.toy_store import ToyStore

class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.store = ToyStore()

    def test_valid__init(self):
        for key in range(ord("A"), ord("G") + 1):
            self.assertIsNone(self.store.toy_shelf[chr(key)])

        self.assertEqual(7, len(self.store.toy_shelf))

    def test_add_toy_in_non_existing_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("K", "New toy")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_that_is_already_exists_on_shelf_raises_exception(self):
        self.store.add_toy("A", "Some toys")

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Some toys")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_to_a_full_shelf_raises_exception(self):
        self.store.add_toy("B", "Dog")

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("B", "Cat")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_successfully_returns_string(self):
        result = self.store.add_toy("B", "Dog")
        self.assertEqual("Dog", self.store.toy_shelf["B"])
        self.assertEqual("Toy:Dog placed successfully!", result)

    def test_remove_toy_from_non_existing_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("Z", "Doll")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_non_existing_toy_from_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "Car")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_successfully(self):
        self.store.toy_shelf["A"] = "Dog"

        result = self.store.remove_toy("A", "Dog")

        self.assertIsNone(self.store.toy_shelf["A"])
        self.assertEqual("Remove toy:Dog successfully!", result)


if __name__ == '__main__':
    main()