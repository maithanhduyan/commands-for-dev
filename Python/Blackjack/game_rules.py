def calculate_hand_value(hand):
    value = 0
    aces = 0
    
    rank_values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 10, 'Q': 10, 'K': 10, 'A': 11
    }
    
    for card in hand:
        if card.rank in rank_values:
            value += rank_values[card.rank]
        if card.rank == 'A':
            aces += 1

    # Adjust for aces if the value is over 21
    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value


def is_bust(hand):
    return calculate_hand_value(hand) > 21

def determine_winner(player_hand, dealer_hand):
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if player_value > 21:
        return "Dealer"
    elif dealer_value > 21 or player_value > dealer_value:
        return "Player"
    elif dealer_value > player_value:
        return "Dealer"
    else:
        return "Tie"
