import unittest
from unittest.mock import patch
from classes.deck import Deck
from classes.player import Player
from blackjack import BlackjackGame

class TestBlackjackGame(unittest.TestCase):
    def setUp(self):
        self.game = BlackjackGame()

    def test_initial_deal(self):
        self.game.deal_initial_cards()
        self.assertEqual(len(self.game.player.hand), 2)
        self.assertEqual(len(self.game.dealer.hand), 2)

    @patch("builtins.input", side_effect=["h", "s"])  # Simulate Hit then Stay
    def test_player_turn_hit_stay(self, mock_input):
        self.game.deal_initial_cards()
        initial_hand_size = len(self.game.player.hand)
        self.game.player_turn()
        self.assertGreater(len(self.game.player.hand), initial_hand_size)

    @patch("builtins.input", side_effect=["s"])  # Simulate Stay
    def test_player_turn_stay(self, mock_input):
        self.game.deal_initial_cards()
        initial_hand_size = len(self.game.player.hand)
        self.game.player_turn()
        self.assertEqual(len(self.game.player.hand), initial_hand_size)

    def test_dealer_turn(self):
        self.game.deal_initial_cards()
        self.game.dealer_turn()
        self.assertGreaterEqual(self.game.dealer.score, 17)

    def test_game_play(self):
        with patch("builtins.input", side_effect=["h", "s"]):
            self.game.play()
            # Ensure player and dealer finish with valid hands
            self.assertGreater(len(self.game.player.hand), 0)
            self.assertGreater(len(self.game.dealer.hand), 0)

if __name__ == "__main__":
    unittest.main()
