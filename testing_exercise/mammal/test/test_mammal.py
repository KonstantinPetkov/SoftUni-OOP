import unittest
from project.mammal import Mammal


class TestMammal(unittest.TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal("Pesho", "dog", "bark")

    def test_valid_initializing(self):
        self.assertEqual("Pesho", self.mammal.name)
        self.assertEqual("dog", self.mammal.type)
        self.assertEqual("bark", self.mammal.sound)

    def test_make_sound_return_correct_message(self):
        self.assertEqual("Pesho makes bark", self.mammal.make_sound())

    def test_get_kingdom_return_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_if_info_return_correct_type(self):
        self.assertEqual("Pesho is of type dog", self.mammal.info())

if __name__ == '__main__':
    unittest.main()