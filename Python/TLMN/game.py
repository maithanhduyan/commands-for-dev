from entities.table import Table
from entities.player import Player
from game_rules import GameRules
from use_cases.play_card_use_case import PlayCardUseCase # Ví dụ use case


from ai.ai_player import AIPlayer
from ai.ml_model import MLModel

# ... (Khởi tạo model ML)
ml_model = MLModel()

# ... (Tạo AI Player)
ai_player = AIPlayer("AI Player", ml_model)

class Game:
    def __init__(self):
        self.table = Table()
        self.game_rules = GameRules()
        self.play_card_use_case = PlayCardUseCase(self.game_rules) 

    def start_game(self):
        """Bắt đầu trò chơi."""
        print('Bắt đầu trò chơi.')
        # ... (Khởi tạo người chơi, chia bài, ...)

    def play_round(self):
        """Chơi một vòng."""
        print('Chơi một vòng.')
        # ... (Lấy input từ người chơi, 
        #      gọi use case để xử lý logic đánh bài, ...)

    def end_game(self):
        """Kết thúc trò chơi."""
        # ... (Tính toán điểm, hiển thị kết quả)

# Khởi chạy trò chơi
if __name__ == "__main__":
    
    game = Game()

    # ... (Thêm AI Player vào bàn chơi)
    game.table.players.append(ai_player)
    game.start_game()
    while True:
        game.play_round()
        # Điều kiện kết thúc trò chơi:
        if():
            game.end_game()
            break