import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):
    def setUp(self):
        self.card = Card("Spades", 1)
        self.card_2 = Card("Hearts", 2)

        self.cards = [self.card, self.card_2]

        self.game = CardGame()
    
    def test_check_for_ace_true(self):
        actual = self.game.checkforAce(self.card)
        self.assertTrue(actual)


    def test_check_for_ace_false(self):
        actual = self.game.checkforAce(self.card_2)
        self.assertFalse(actual)


    def test_card_2_is_higher_than_card_1_return_card_1(self):
        expected = self.card_2
        actual = self.game.highest_card(self.card_2, self.card)
        self.assertEqual(expected, actual)


    def test_card_has_total_of_2(self):
        actual = self.game.cards_total(self.cards)
        self.assertEqual("You have a total of 2", actual)