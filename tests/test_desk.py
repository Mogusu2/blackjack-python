import unittest
from classes.deck import Deck
from classes.card import Card

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_initialization(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_deck_shuffle(self):
        # Copy the deck and shuffle
        original_order = list(self.deck.cards)
        self.deck.shuffle()
        self.assertNotEqual(original_order, self.deck.cards)

    def test_draw_card(self):
        card = self.deck.draw_card()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(self.deck.cards), 51)

    def test_draw_card_empty_deck(self):
        for _ in range(52):
            self.deck.draw_card()
        with self.assertRaises(ValueError):
            self.deck.draw_card()

if __name__ == "__main__":
    unittest.main()
