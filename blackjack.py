from classes.deck import Deck
from classes.player import Player
from utils.display import display_cards, display_message

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Player("Dealer")

    def deal_initial_cards(self):
        """
        Deal two cards to both the player and the dealer.
        """
        for _ in range(2):
            self.player.add_card(self.deck.draw_card())
            self.dealer.add_card(self.deck.draw_card())

    def player_turn(self):
        """
        Handle the player's turn, allowing them to hit or stay.
        """
        while True:
            display_cards(self.player)
            action = input("Do you want to [H]it or [S]tay? ").strip().lower()
            if action == 'h':
                self.player.add_card(self.deck.draw_card())
                if self.player.is_busted():
                    display_message("You busted!", "bold red")
                    break
            elif action == 's':
                display_message("You chose to stay.", "bold green")
                break

    def dealer_turn(self):
        """
        Handle the dealer's turn, which is automated.
        """
        while self.dealer.score < 17:
            self.dealer.add_card(self.deck.draw_card())
        if self.dealer.is_busted():
            display_message("Dealer busted!", "bold red")

    def determine_winner(self):
        """
        Determine the winner based on the final scores.
        """
        display_message("\nFinal Results:")
        display_cards(self.player)
        display_cards(self.dealer)

        if self.player.is_busted():
            display_message("Dealer wins! (Player busted)", "bold red")
        elif self.dealer.is_busted():
            display_message("Player wins! (Dealer busted)", "bold green")
        elif self.player.score > self.dealer.score:
            display_message("Player wins!", "bold green")
        elif self.player.score < self.dealer.score:
            display_message("Dealer wins!", "bold red")
        else:
            display_message("It's a tie!", "bold yellow")

    def play(self):
        """
        Run the game loop.
        """
        display_message("Welcome to Blackjack!", "bold cyan")
        self.deal_initial_cards()
        self.player_turn()
        if not self.player.is_busted():
            self.dealer_turn()
        self.determine_winner()

if __name__ == "__main__":
    game = BlackjackGame()
    game.play()
