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

