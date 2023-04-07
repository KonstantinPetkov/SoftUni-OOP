from project.band_members.musician import Musician


VALID_SKILLS = ("sing high pitch notes", "sing low pitch notes")


class Singer(Musician):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.valid_skills = VALID_SKILLS
