
class Player:
    def __init__(self, name, is_dealer=False):
        self.name = name
        self.hand = []
        self.is_dealer = is_dealer

    def draw_card(self, deck):
        self.hand.append(deck.draw())
