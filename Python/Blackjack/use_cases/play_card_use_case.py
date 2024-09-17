from entities.table import Table
from game_rules import calculate_hand_value, determine_winner

def play_card(table):
    table.player.draw_card(table.deck)
    if calculate_hand_value(table.player.hand) > 21:
        print("Player busts!")
        return determine_winner(table.player.hand, table.dealer.hand)
    return None
