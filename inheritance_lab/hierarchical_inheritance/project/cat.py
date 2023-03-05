from project.animal import Animal


class Cat(Animal):
    def meow(self):
        return 'meowing...'


animal = Cat()
print(animal.eat())
print(animal.meow())