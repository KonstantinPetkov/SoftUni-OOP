from unittest import TestCase,main
from project.shopping_cart import ShoppingCart

class TestShopping(TestCase):

    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart("Lidl", 100)
        self.shops = {
            "Product one": 10,
            "Product two": 10,
        }

    def test_correct__init(self):
        self.assertEqual("Lidl", self.shopping_cart.shop_name)
        self.assertEqual(100, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_invalid_shop_name_set_raises_error(self):
        with self.assertRaises(ValueError) as err:
            self.shopping_cart.shop_name = "shop"

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(err.exception))

    def test_not_add_to_card_raises_error(self):
        with self.assertRaises(ValueError) as err:
            self.shopping_cart.add_to_cart("Book", 100)

        self.assertEqual("Product Book cost too much!", str(err.exception))

    def test_successful_add_to_cart(self):
        result = self.shopping_cart.add_to_cart("Toy", 10)
        self.assertEqual("Toy product was successfully added to the cart!", result)

        self.assertEqual({"Toy": 10}, self.shopping_cart.products)

    def test_successful_remove_from_cart(self):
        self.shopping_cart.products = self.shops

        result = self.shopping_cart.remove_from_cart("Product two")
        self.assertEqual({"Product one": 10}, self.shopping_cart.products)
        self.assertEqual("Product Product two was successfully removed from the cart!", result)

    def test_unsuccessful_remove_from_cart_raises_error(self):
        with self.assertRaises(ValueError) as err:
            self.shopping_cart.remove_from_cart("New product")

        self.assertEqual("No product with name New product in the cart!", str(err.exception))

    def test___add__(self):
        first_instance = ShoppingCart("First", 50)
        first_instance.products = {"Car": 25}

        second_instance = ShoppingCart("Second", 20)
        second_instance.products = {"Dog": 5}

        merged_instance = first_instance + second_instance
        merged_products = {"Car": 25, "Dog": 5}

        self.assertEqual("FirstSecond", merged_instance.shop_name)
        self.assertEqual(70, merged_instance.budget)
        self.assertEqual(merged_products, merged_instance.products)

    def test_unsuccessful_buy_products_raises_error(self):
        self.shopping_cart.products = {"Milk": 100, "Bread": 120}
        total_sum = sum(self.shopping_cart.products.values())

        with self.assertRaises(ValueError) as err:
            self.shopping_cart.buy_products()

        self.assertEqual(f"Not enough money to buy the products! Over budget with {total_sum - self.shopping_cart.budget:.2f}lv!", str(err.exception))

    def test_successful_buy_products(self):
        self.shopping_cart.products = {"Coconut": 30, "Bread": 20}
        total_sum = sum(self.shopping_cart.products.values())
        result = self.shopping_cart.buy_products()

        self.assertEqual(f'Products were successfully bought! Total cost: {total_sum:.2f}lv.', result)


if __name__ == '__main__':
    main()
