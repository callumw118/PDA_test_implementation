import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):
    def setUp(self):
        self.card = Card("Spades", 1)
        self.card_2 = Card("Hearts", 2)
        self.game = CardGame()
    
    def test_check_for_ace_true(self):
        actual = self.game.checkforAce(self.card)
        self.assertTrue(actual)

    def test_check_for_ace_false(self):
        actual = self.game.checkforAce(self.card_2)
        self.assertFalse(actual)