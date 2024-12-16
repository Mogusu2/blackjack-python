from rich.console import Console
from rich.table import Table

console = Console()

def display_cards(player):
    """
    Beautify and display a player's hand in a table format.

    :param player: The Player object whose hand will be displayed.
    """
    table = Table(title=f"{player.name}'s Hand", show_header=True, header_style="bold magenta")
    table.add_column("Card", justify="center")
    table.add_column("Value", justify="center")

    for card in player.hand:
        table.add_row(str(card), str(card.value))

    console.print(table)

def display_message(message, style="bold cyan"):
    """
    Display a styled message in the terminal.

    :param message: The message to display.
    :param style: The style to apply (default: bold cyan).
    """
    console.print(message, style=style)
