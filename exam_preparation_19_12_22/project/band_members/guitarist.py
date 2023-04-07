from project.band_members.musician import Musician


VALID_SKILLS = ("play metal", "play rock", "play jazz")


class Guitarist(Musician):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.valid_skills = VALID_SKILLS
