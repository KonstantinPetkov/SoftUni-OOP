from project import client
from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:

    VALID_MEALS = (
        "Starter",
        "MainDish",
        "Dessert",
    )

    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 1

    def register_client(self, client_phone_number: str):
        try:
            client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        except StopIteration:
            raise Exception("The client has already been registered!")

        self.clients_list.append(client.client_phone_number)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        meals = [meal for meal in meals if meal.__class__.__name__ in self.VALID_MEALS]
        self.menu.append(meals)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return '\n'.join(str(meal.details()) for meal in self.menu)

    def __get_or_create_client(self, client_phone_number):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                return client

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return new_client

    def __get_menu(self):
        return {meal.name: meal for meal in self.menu}

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        find_client = self.__get_or_create_client(client_phone_number)
        menu_info = self.__get_menu()

        for meal in meal_names_and_quantities:
            if meal not in self.menu:
                raise Exception(f"{meal.meal_name} is not on the menu!")

        for meal_name, quantity in meal_names_and_quantities.items():
            if menu_info[meal_name].quantity < quantity:
                raise Exception(f"Not enough quantity of {menu_info[meal].__class__.__name__}: {meal}!")

        for meal_name, quantity in meal_names_and_quantities.items():
            menu_info[meal_name].quantity -= quantity
            find_client.shopping_cart.append(menu_info[meal_name])

        find_client.bill += sum(menu_info[name].price * quantity for name, quantity in meal_names_and_quantities.items())
        find_client.ordered_meals.update(meal_names_and_quantities)

        return f"Client {client_phone_number} successfully ordered {', '.join(find_client.ordered_meals)} for {find_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        new_client = self.__get_or_create_client(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        menu_info = self.__get_menu()

        for name, qty in new_client.ordered_meals.items():
            menu_info[name].quantity += qty

        new_client.bill = 0
        new_client.shopping_cart = []
        new_client.ordered_meals = {}

        return f"Client {new_client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        new_client = self.__get_or_create_client(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        current_receipt_id = self.receipt_id
        self.receipt_id += 1
        total_bill = new_client.bill

        new_client.bill = 0
        new_client.shopping_cart = []
        new_client.ordered_meals = {}

        return f"Receipt #{current_receipt_id} with total amount of {total_bill:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len((self.menu))} meals on the menu and {len(self.clients_list)} clients."