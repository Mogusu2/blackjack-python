# utils/display.py
from rich.console import Console
from rich.table import Table

console = Console()

def display_cards(player):
    """
    Beautify and display a player's hand in a table format.
    """
    table = Table(title=f"[bold magenta]{player.name}'s Hand[/bold magenta]", show_header=True, header_style="bold magenta")
    table.add_column("Card", justify="center")
    table.add_column("Value", justify="center")

    for card in player.hand:
        table.add_row(str(card), str(card.value))

    console.print(table)

def display_dealer_hand(dealer, show_first_card=True):
    """
    Beautify and display the dealer's hand with one card hidden if specified.
    """
    table = Table(title=f"[bold red]{dealer.name}'s Hand[/bold red]", show_header=True, header_style="bold red")
    table.add_column("Card", justify="center")
    table.add_column("Value", justify="center")

    if show_first_card:
        # Only show the first card and hide the second one
        table.add_row(str(dealer.hand[0]), str(dealer.hand[0].value))
        table.add_row("[bold green]Hidden Card[/bold green]", "[bold green]??[/bold green]")
    else:
        # Show both cards after the dealer's turn
        for card in dealer.hand:
            table.add_row(str(card), str(card.value))

    console.print(table)

def display_message(message, style="bold cyan"):
    """
    Display a styled message in the terminal.
    """
    console.print(message, style=style)
