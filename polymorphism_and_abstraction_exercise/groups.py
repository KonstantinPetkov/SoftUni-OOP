from typing import List


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = List[Person]

    def __len__(self):
        return len(self.people)

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"



