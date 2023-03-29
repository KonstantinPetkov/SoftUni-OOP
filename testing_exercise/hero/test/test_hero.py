import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self) -> None:
        self.hero = Hero("Hero", 1, 200, 200)
        self.enemy = Hero("Enemy", 1, 100, 100)

    def test_valid_initializing(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(200, self.hero.health)
        self.assertEqual(200, self.hero.damage)

    def test_battle_hero_is_same_as_enemy(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_fight_hero_with_zero_energy(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as err:
            self.hero.battle(self.enemy)
        self.assertEqual(str(err.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_fight_hero_with_enemy_with_zero_energy(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as err:
            self.hero.battle(self.enemy)
        self.assertEqual(str(err.exception), "You cannot fight Enemy. He needs to rest")

    def test_battle_health_and_damage_removed_after_fight_is_draw(self):
        self.hero.health = self.enemy.health
        self.hero.damage = self.enemy.damage

        result = self.hero.battle(self.enemy)

        self.assertEqual(self.hero.health, 0)
        self.assertEqual(self.enemy.health, 0)
        self.assertEqual("Draw", result)

    def test_battle_enemy_and_win(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 105)
        self.assertEqual(self.hero.damage, 205)
        self.assertEqual("You win", result)

    def test_battle_enemy_and_lose(self):
        self.hero, self.enemy = self.enemy, self.hero

        result = self.hero.battle(self.enemy)

        self.assertEqual(self.enemy.level, 2)
        self.assertEqual(self.enemy.health, 105)
        self.assertEqual(self.enemy.damage, 205)
        self.assertEqual("You lose", result)

    def test_valid__str__(self):
        self.assertEqual(str(self.hero),
                        "Hero Hero: 1 lvl\n" +
                        "Health: 200\n" +
                        "Damage: 200\n" )


if __name__ == '__main__':
    unittest.main()