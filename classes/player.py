# player.py
from classes.card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def add_card(self, card: Card):
        """
        Add a card to the player's hand and update the score.
        """
        self.hand.append(card)
        self.update_score()

    def update_score(self):
        """
        Calculate the score based on the cards in hand, adjusting for Aces.
        """
        self.score = sum(card.value for card in self.hand)

        # Adjust for Aces only if score > 21
        ace_count = sum(1 for card in self.hand if card.rank == 'Ace')
        while self.score > 21 and ace_count > 0:
            self.score -= 10
            ace_count -= 1

    def display_hand(self):
        """
        Return a formatted string representing the player's hand and score.
        """
        hand_representation = ', '.join([str(card) for card in self.hand])
        return f"{self.name}'s Hand: {hand_representation} (Score: {self.score})"


    def is_busted(self):
        """
        Check if the player has busted (score > 21).
        """
        return self.score > 21

    def __str__(self):
        return f"{self.name} ({self.score} points)"
