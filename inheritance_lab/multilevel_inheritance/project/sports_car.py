from project.car import Car


class SportsCar(Car):
    def race(self):
        return "racing..."

car = SportsCar()
print(car.move())
print(car.drive())
print(car.race())