from project.animal import Animal


class Cheetah(Animal):
    CHEETAH_NEEDS = 60

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Cheetah.CHEETAH_NEEDS)