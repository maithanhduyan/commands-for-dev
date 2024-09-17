# You are an intelligent programming assistant.
# This is nodejs project

# Directory tree of C:\Users\tiach\Downloads\commands-for-dev\Python\Blackjack

├── Blackjack/
│   ├── analytic.py
│   ├── game.py
│   ├── game_rules.py
│   └── requirements.txt
│   ├── .vscode/
│   │   └── launch.json
│   ├── ai/
│   │   ├── ai_player.py
│   │   └── ml_model.py
│   ├── assets/
│   │   ├── 10_of_Clubs.png
│   │   ├── 10_of_Diamonds.png
│   │   ├── 10_of_Hearts.png
│   │   ├── 10_of_Spades.png
│   │   ├── 2_of_Clubs.png
│   │   ├── 2_of_Diamonds.png
│   │   ├── 2_of_Hearts.png
│   │   ├── 2_of_Spades.png
│   │   ├── 3_of_Clubs.png
│   │   ├── 3_of_Diamonds.png
│   │   ├── 3_of_Hearts.png
│   │   ├── 3_of_Spades.png
│   │   ├── 4_of_Clubs.png
│   │   ├── 4_of_Diamonds.png
│   │   ├── 4_of_Hearts.png
│   │   ├── 4_of_Spades.png
│   │   ├── 5_of_Clubs.png
│   │   ├── 5_of_Diamonds.png
│   │   ├── 5_of_Hearts.png
│   │   ├── 5_of_Spades.png
│   │   ├── 6_of_Clubs.png
│   │   ├── 6_of_Diamonds.png
│   │   ├── 6_of_Hearts.png
│   │   ├── 6_of_Spades.png
│   │   ├── 7_of_Clubs.png
│   │   ├── 7_of_Diamonds.png
│   │   ├── 7_of_Hearts.png
│   │   ├── 7_of_Spades.png
│   │   ├── 8_of_Clubs.png
│   │   ├── 8_of_Diamonds.png
│   │   ├── 8_of_Hearts.png
│   │   ├── 8_of_Spades.png
│   │   ├── 9_of_Clubs.png
│   │   ├── 9_of_Diamonds.png
│   │   ├── 9_of_Hearts.png
│   │   ├── 9_of_Spades.png
│   │   ├── A_of_Clubs.png
│   │   ├── A_of_Diamonds.png
│   │   ├── A_of_Hearts.png
│   │   ├── A_of_Spades.png
│   │   ├── back_of_card.png
│   │   ├── Joker_of_card.png
│   │   ├── J_of_Clubs.png
│   │   ├── J_of_Diamonds.png
│   │   ├── J_of_Hearts.png
│   │   ├── J_of_Spades.png
│   │   ├── K_of_Clubs.png
│   │   ├── K_of_Diamonds.png
│   │   ├── K_of_Hearts.png
│   │   ├── K_of_Spades.png
│   │   ├── Q_of_Clubs.png
│   │   ├── Q_of_Diamonds.png
│   │   ├── Q_of_Hearts.png
│   │   └── Q_of_Spades.png
│   ├── entities/
│   │   ├── card.py
│   │   ├── player.py
│   │   └── table.py
│   ├── gui/
│   │   ├── game_view.py
│   │   └── gui_handler.py
│   ├── use_cases/
│   │   └── play_card_use_case.py

## C:\Users\tiach\Downloads\commands-for-dev\Python\Blackjack\game.py
```
from entities.table import Table
from gui.game_view import GameView

def main():
    table = Table()
    game_view = GameView(table)

    while not table.is_game_over():
        game_view.render()
        table.play_round()
        game_view.render()

        # Wait for player input to continue
        game_view.display_message("Press Enter to continue", (300, 500))
        input()  # Wait for the player to press Enter

        # Reset the round for the next one
        table.reset_round()

if __name__ == "__main__":
    main()

```

## C:\Users\tiach\Downloads\commands-for-dev\Python\Blackjack\game_rules.py
```
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

```

## C:\Users\tiach\Downloads\commands-for-dev\Python\Blackjack\requirements.txt
```
pygame
```

## C:\Users\tiach\Downloads\commands-for-dev\Python\Blackjack\ai\ai_player.py
```
class AIPlayer:
    def __init__(self, model):
        self.model = model

    def make_decision(self, hand):
        # Use model to decide whether to hit or stand
        pass

```

## C:\Users\tiach\Downloads\commands-for-dev\Python\Blackjack\ai\ml_model.py
```
class MLModel:
    def __init__(self):
        # Initialize your model (e.g., load pre-trained model)
        pass

    def predict(self, state):
        # Return action based on model prediction
        pass

```

## C:\Users\tiach\Downloads\commands-for-dev\Python\Blackjack\entities\card.py
```
import random

class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, rank):
        if suit not in Card.suits:
            raise ValueError(f"Invalid suit: {suit}")
        if rank not in Card.ranks:
            raise ValueError(f"Invalid rank: {rank}")
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


```

## C:\Users\tiach\Downloads\commands-for-dev\Python\Blackjack\entities\player.py
```

class Player:
    def __init__(self, name, is_dealer=False):
        self.name = name
        self.hand = []
        self.is_dealer = is_dealer

    def draw_card(self, deck):
        self.hand.append(deck.draw())

```

## C:\Users\tiach\Downloads\commands-for-dev\Python\Blackjack\entities\table.py
```
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

```

## C:\Users\tiach\Downloads\commands-for-dev\Python\Blackjack\gui\game_view.py
```
import pygame
from entities.card import Card

class GameView:
    def __init__(self, table):
        self.table = table
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Blackjack")

        # Load assets
        self.card_images = self.load_card_images()
        self.background_color = (0, 128, 0)  # Green background like a casino table
        self.font = pygame.font.SysFont(None, 36)

    def load_card_images(self):
        card_images = {}
        for suit in Card.suits:
            for rank in Card.ranks:
                image_path = f"assets/{rank}_of_{suit}.png"
                card_images[(rank, suit)] = pygame.image.load(image_path)
        return card_images

    def render(self):
        self.screen.fill(self.background_color)

        # Render dealer's hand
        self.render_hand(self.table.dealer.hand, (100, 100), hidden=self.table.dealer.is_dealer)

        # Render player's hand
        self.render_hand(self.table.player.hand, (100, 400))

        # Render text for winner
        if self.table.winner:
            winner_text = self.font.render(f"The winner is: {self.table.winner}", True, (255, 255, 255))
            self.screen.blit(winner_text, (300, 50))

        # Update the display
        pygame.display.flip()

    def render_hand(self, hand, position, hidden=False):
        x, y = position
        for index, card in enumerate(hand):
            if hidden and index == 1:
                card_image = pygame.image.load("assets/back_of_card.png")
            else:
                card_image = self.card_images[(card.rank, card.suit)]
            self.screen.blit(card_image, (x + index * 80, y))

    def display_message(self, message, position):
        text = self.font.render(message, True, (255, 255, 255))
        self.screen.blit(text, position)
        pygame.display.flip()


```

## C:\Users\tiach\Downloads\commands-for-dev\Python\Blackjack\gui\gui_handler.py
```
import pygame

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

```

## C:\Users\tiach\Downloads\commands-for-dev\Python\Blackjack\use_cases\play_card_use_case.py
```
from entities.table import Table
from game_rules import calculate_hand_value, determine_winner

def play_card(table):
    table.player.draw_card(table.deck)
    if calculate_hand_value(table.player.hand) > 21:
        print("Player busts!")
        return determine_winner(table.player.hand, table.dealer.hand)
    return None

```

