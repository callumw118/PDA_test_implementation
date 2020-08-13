import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):
    def setUp(self):
        self.card = Card("Spades", 1)
    
    def test_check_for_ace(self):
        actual = CardGame.checkforAce(self.card)
        self.assertTrue(actual)