import unittest
from classes.card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", "Ace", 11)

    def test_card_initialization(self):
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.rank, "Ace")
        self.assertEqual(self.card.value, 11)

    def test_card_string_representation(self):
        self.assertEqual(str(self.card), "Ace of Hearts")

if __name__ == "__main__":
    unittest.main()
