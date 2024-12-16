import random
from classes.card import Card

class Deck:
    def __init__(self):
        """
        Initialize the deck with 52 shuffled cards.
        """
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                  'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        self.cards = [Card(suit, rank, values[rank]) for suit in suits for rank in ranks]
        self.shuffle()

    def shuffle(self):
        """
        Shuffle the deck.
        """
        random.shuffle(self.cards)

    def draw_card(self):
        """
        Draw a card from the deck. Raises an exception if the deck is empty.
        """
        if not self.cards:
            raise ValueError("The deck is empty!")
        return self.cards.pop()
