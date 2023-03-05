class PizzaDelivery:
    ordered = False

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not PizzaDelivery.ordered:
            if ingredient not in self.ingredients:
                self.ingredients[ingredient] = 0
            self.ingredients[ingredient] += quantity
            self.price += price_per_quantity * quantity

        return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not PizzaDelivery.ordered:
            if ingredient not in self.ingredients:
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
            if self.ingredients[ingredient] < quantity:
                return f"Please check again the desired quantity of {ingredient}!"
            self.ingredients[ingredient] -= quantity
            self.price -= price_per_quantity * quantity

        return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def make_order(self):
        if not PizzaDelivery.ordered:
            PizzaDelivery.ordered = True
            some_ingredient = [f"{key}: {value}" for key, value in self.ingredients.items()]
            return f"You've ordered pizza {self.name} prepared with {', '.join(some_ingredient)} and the price will be {self.price}lv."

        return f"Pizza {self.name} already prepared, and we can't make any changes!"



margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
