from typing import List

from project import band
from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:

    VALID_MUSICIAN_TYPE = [
        "Guitarist",
        "Drummer",
        "Singer",
    ]

    VALID_MUSICIAN_NAME = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer,
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPE:
            raise ValueError("Invalid musician type!")

        musician_name_list = [m.name for m in self.musicians]
        if name in musician_name_list:
            raise Exception(f"{name} is already a musician!")

        musician = self.VALID_MUSICIAN_NAME[musician_type](name, age)
        self.musicians.append(musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band_name = [b.name for b in self.bands]
        if name in band_name:
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        existing_concert_place = [c for c in self.concerts if c.place == place]
        if existing_concert_place:
            raise Exception(f"{place} is already registered for {genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            musician = next(filter(lambda m: m.name == musician_name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            bands = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        bands.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            existing_bands = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musicians = list(filter(lambda m: m.name == musician_name, existing_bands.members))
        except IndexError:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        musician = musicians[0]
        existing_bands.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        check_band = [b for b in self.bands if b.name == band_name][0]
        check_concert = [c for c in self.concerts if c.place == concert_place][0]

        singers = [m for m in check_band.members if isinstance(m, Singer)]
        drummers = [m for m in check_band.members if isinstance(m, Drummer)]
        guitarists = [m for m in check_band.members if isinstance(m, Guitarist)]

        if not (singers and drummers and guitarists):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        are_drummer_qualified = True
        are_singer_qualified = True
        are_guitarist_qualified = True

        for drummer in drummers:
            if check_concert.genre == "Rock":
                if "play the drums with drumsticks" not in drummer.valid_skills:
                    are_drummer_qualified = False
            elif check_concert.genre == "Metal":
                if "play the drums with drumsticks" not in drummer.valid_skills:
                    are_drummer_qualified = False
            else:
                if "play the drums with drum brushes" not in drummer.valid_skills:
                    are_drummer_qualified = False

        for singer in singers:
            if check_concert.genre == "Rock":
                if "sing high pitch notes" not in singer.valid_skills:
                    are_singer_qualified = False
            elif check_concert.genre == "Metal":
                if "sing low pitch notes" not in singer.valid_skills:
                    are_singer_qualified = False
            else:
                if "sing high pitch notes" not in singer.valid_skills or "sing low pitch notes " not in singer.valid_skills:
                    are_singer_qualified = False

        for guitarist in guitarists:
            if check_concert.genre == "Rock":
                if "play rock" not in guitarist.valid_skills:
                    are_guitarist_qualified = False
            elif check_concert.genre == "Metal":
                if "play metal" not in guitarist.valid_skills:
                    are_guitarist_qualified = False
            else:
                if "play jazz" not in guitarist.valid_skills:
                    are_guitarist_qualified = False

        if not are_drummer_qualified or not are_singer_qualified or not are_guitarist_qualified:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (check_concert.audience * check_concert.ticket_price) - check_concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {check_concert.genre} concert in {check_concert.place}."