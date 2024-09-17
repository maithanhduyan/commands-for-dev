from entities.player import Player
from entities.card import Deck
from game_rules import calculate_hand_value, is_bust, determine_winner

class Table:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Player("Dealer", is_dealer=True)
        self.deck.shuffle()
        self.round_over = False
        self.winner = None

    def deal_initial_cards(self):
        for _ in range(2):
            self.player.draw_card(self.deck)
            self.dealer.draw_card(self.deck)
        print(f"Player's initial hand: {[(card.rank, card.suit) for card in self.player.hand]}")
        print(f"Dealer's initial hand: {[(self.dealer.hand[0].rank, self.dealer.hand[0].suit), ('Hidden', 'Card')]}")

    def player_turn(self):
        # Player decides whether to hit or stand
        while True:
            print(f"Player's hand: {[(card.rank, card.suit) for card in self.player.hand]}")
            move = input("Do you want to hit (h) or stand (s)? ").lower()
            if move == 'h':
                self.player.draw_card(self.deck)
                print(f"Player drew: {self.player.hand[-1].rank} of {self.player.hand[-1].suit}")
                if is_bust(self.player.hand):
                    print("Player busts!")
                    self.winner = "Dealer"
                    return
            elif move == 's':
                print("Player stands.")
                break

    def dealer_turn(self):
        print(f"Dealer's hidden card: {self.dealer.hand[1].rank} of {self.dealer.hand[1].suit}")
        print(f"Dealer's hand: {[(card.rank, card.suit) for card in self.dealer.hand]}")
        while calculate_hand_value(self.dealer.hand) < 17:
            print("Dealer hits.")
            self.dealer.draw_card(self.deck)
            print(f"Dealer drew: {self.dealer.hand[-1].rank} of {self.dealer.hand[-1].suit}")
            print(f"Dealer's hand: {[(card.rank, card.suit) for card in self.dealer.hand]}")
        if is_bust(self.dealer.hand):
            print("Dealer busts!")
            self.winner = "Player"

    def determine_winner(self):
        if not self.winner:
            self.winner = determine_winner(self.player.hand, self.dealer.hand)
        print(f"The winner is: {self.winner}")

    def reset_round(self):
        self.player.hand = []
        self.dealer.hand = []
        self.deck = Deck()
        self.deck.shuffle()
        self.round_over = False
        self.winner = None

    def play_round(self):
        # 1. Deal initial cards to both player and dealer
        self.deal_initial_cards()

        # 2. Player's turn to decide whether to hit or stand
        self.player_turn()

        # 3. If the player has not busted, the dealer takes their turn
        if not self.winner:
            self.dealer_turn()

        # 4. Determine the winner of the round
        self.determine_winner()

        # 5. Set the round as over
        self.round_over = True

    def is_game_over(self):
        # Implement your own logic to decide when the game is over
        return False
