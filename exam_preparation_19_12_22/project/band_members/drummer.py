from project.band_members.musician import Musician


VALID_SKILLS = ("play the drums with drumsticks", "play the drums with drum brushes", "read sheet music")


class Drummer(Musician):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.valid_skills = VALID_SKILLS
