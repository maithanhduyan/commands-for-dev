from entities.player import Player

class AIPlayer(Player):
    """Người chơi AI."""
    def __init__(self, name, ml_model):
        super().__init__(name)
        self.ml_model = ml_model

    def choose_cards_to_play(self, table):
        """Chọn bài để đánh dựa trên model ML.
        
        Args:
            table: Bàn chơi hiện tại.

        Returns:
            Danh sách các lá bài được chọn, hoặc None nếu bỏ lượt.
        """
        # Lấy thông tin cần thiết từ bàn chơi
        # ... (ví dụ: bài trên bàn, bài của người chơi khác, ...)

        # Sử dụng ml_model để dự đoán hành động tốt nhất
        chosen_cards = self.ml_model.predict(game_state)

        return chosen_cards