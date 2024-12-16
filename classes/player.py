class Player:
    def __init__(self, name):
        """
        Initialize a player with a name, an empty hand, and a score of 0.

        :param name: The name of the player (e.g., "Player", "Dealer").
        """
        self.name = name
        self.hand = []
        self.score = 0

    def add_card(self, card):
        """
        Add a card to the player's hand and update their score.

        :param card: The card to add.
        """
        self.hand.append(card)
        self.update_score()

    def update_score(self):
        """
        Calculate the score based on the cards in hand, adjusting for Aces.
        """
        self.score = sum(card.value for card in self.hand)
        # Adjust for Aces
        for card in self.hand:
            if self.score > 21 and card.rank == 'Ace':
                self.score -= 10

    def display_hand(self):
        """
        Return a formatted string representing the player's hand and score.
        """
        hand_representation = ', '.join([str(card) for card in self.hand])
        return f"{self.name}'s Hand: {hand_representation} (Score: {self.score})"

    def is_busted(self):
        """
        Check if the player has gone over 21.
        """
        return self.score > 21
