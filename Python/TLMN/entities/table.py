import random
from entities.card import Card

class Table:
    """
    Biểu diễn bàn chơi.
    """
    def __init__(self, num_players=4):
        """
        Khởi tạo bàn chơi.

        Args:
          num_players: Số lượng người chơi (mặc định là 4).
        """
        self.num_players = num_players
        self.players = []
        self.deck = [] # Bộ bài
        self.current_player = None # Người chơi hiện tại
        self.last_played_cards = [] # Nhóm bài vừa đánh

    def create_deck(self):
        """
        Tạo bộ bài 52 lá.
        """
        self.deck = [Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS]

    def shuffle_deck(self):
        """
        Xáo trộn bộ bài.
        """
        random.shuffle(self.deck)

    def deal_cards(self):
        """
        Chia bài cho người chơi.
        """
        for i in range(self.num_players):
            self.players[i].hand = self.deck[i::self.num_players]