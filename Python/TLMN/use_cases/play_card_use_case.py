class PlayCardUseCase:
    def __init__(self, game_rules):
        self.game_rules = game_rules

    def execute(self, player, cards, table):
        """
        Thực hiện use case đánh bài.

        Args:
          player: Người chơi muốn đánh bài.
          cards: Danh sách các lá bài muốn đánh.
          table: Bàn chơi hiện tại.

        Returns:
          Kết quả của việc đánh bài (thành công hay thất bại).
        """
        if not self.game_rules.is_valid_play(cards, table.last_played_cards):
            return False  # Bài đánh không hợp lệ

        # ... (Thực hiện logic đánh bài, cập nhật trạng thái bàn chơi)

        return True