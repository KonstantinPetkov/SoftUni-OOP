from project.food import Food


class Fruit(Food):
    def __init__(self, name, expiration_date):
        super().__init__(expiration_date)
        self.name = name


# fruit = Fruit('Apple', '01-02-2020')
# print(fruit.name)
# print(fruit.expiration_date)

