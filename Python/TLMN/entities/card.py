# 

class Card:
    """
    Biểu diễn một lá bài.
    """
    RANKS = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]
    SUITS = ["♠", "♣", "♦", "♥"]

    def __init__(self, rank, suit):
        """
        Khởi tạo lá bài.

        Args:
          rank: Giá trị lá bài (3, 4, ..., 2).
          suit: Chất của lá bài (♠, ♣, ♦, ♥).
        """
        self.rank = rank
        self.suit = suit

    def __str__(self):
        """
        Trả về chuỗi biểu diễn lá bài.
        """
        return self.rank + self.suit

    def __lt__(self, other):
        """
        So sánh 2 lá bài.
        """
        if self.rank == other.rank:
            return Card.SUITS.index(self.suit) < Card.SUITS.index(other.suit)
        return Card.RANKS.index(self.rank) < Card.RANKS.index(other.rank)