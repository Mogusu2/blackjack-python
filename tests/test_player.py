import unittest
from classes.player import Player
from classes.card import Card

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Test Player")
        self.card1 = Card("Hearts", "5", 5)
        self.card2 = Card("Diamonds", "Ace", 11)
        self.card3 = Card("Clubs", "8", 8)

    def test_player_initialization(self):
        self.assertEqual(self.player.name, "Test Player")
        self.assertEqual(self.player.score, 0)
        self.assertEqual(len(self.player.hand), 0)

    def test_add_card(self):
        self.player.add_card(self.card1)
        self.assertEqual(len(self.player.hand), 1)
        self.assertEqual(self.player.score, 5)

    def test_update_score_with_ace(self):
        self.player.add_card(self.card2)  # Ace as 11
        self.assertEqual(self.player.score, 11)
        self.player.add_card(self.card1)  # Add 5
        self.assertEqual(self.player.score, 16)
        self.player.add_card(Card("Clubs", "8", 8))  # Bust with 8
        self.assertEqual(self.player.score, 14)

    def test_update_score_ace_adjustment(self):
        self.player.add_card(self.card2)  # Ace as 11
        self.player.add_card(Card("Clubs", "9", 9))  # Total 20
        self.assertEqual(self.player.score, 20)
        self.player.add_card(Card("Spades", "7", 7))  # Adjust Ace
        self.assertEqual(self.player.score, 17)

    def test_is_busted(self):
        self.player.add_card(self.card1)  # 5
        self.assertFalse(self.player.is_busted())
        self.player.add_card(Card("Clubs", "10", 10))  # 15
        self.assertFalse(self.player.is_busted())
        self.player.add_card(Card("Spades", "9", 9))  # Bust
        self.assertTrue(self.player.is_busted())

if __name__ == "__main__":
    unittest.main()
