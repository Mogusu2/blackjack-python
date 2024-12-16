class Card:
    def __init__(self, suit, rank, value):
        """
        Initialize a card with suit, rank, and value.

        :param suit: The suit of the card (e.g., Hearts, Diamonds).
        :param rank: The rank of the card (e.g., 2, King, Ace).
        :param value: The numerical value of the card.
        """
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        """
        String representation of the card.
        """
        return f"{self.rank} of {self.suit}"
