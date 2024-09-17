class Player:
    """
    Biểu diễn người chơi.
    """
    def __init__(self, name):
        """
        Khởi tạo người chơi.

        Args:
          name: Tên người chơi.
        """
        self.name = name
        self.hand = []  # Danh sách các lá bài trên tay