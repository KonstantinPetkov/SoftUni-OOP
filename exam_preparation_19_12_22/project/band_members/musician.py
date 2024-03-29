from abc import ABC, abstractmethod


class Musician(ABC):

    @abstractmethod
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []
        self.valid_skills = ()

    @property
    def valid_skills(self):
        return self.__valid_skills

    @valid_skills.setter
    def valid_skills(self, value):
        self.__valid_skills = value

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Musician name cannot be empty!")

        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 16:
            raise ValueError("Musicians should be at least 16 years old!")

        self.__age = value

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.valid_skills:
            raise ValueError(f"{new_skill} is not a needed skill!")

        if new_skill in self.valid_skills:
            raise ValueError(f"{new_skill} is already learned!")

        self.skills.append(new_skill)

        return f"{self.name} learned to {new_skill}."