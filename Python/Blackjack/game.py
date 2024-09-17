import logging
from entities.table import Table
from gui.game_view import GameView
import pygame

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Game started")
    table = Table()
    game_view = GameView(table)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logging.info("Quit event detected")
                running = False

        game_view.render()
        pygame.display.update()  # Cập nhật toàn bộ màn hình
        # table.play_round()

        # Hiển thị thông báo và chờ người dùng nhấn Enter
        game_view.display_message("Press Enter to continue", (300, 500))
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    logging.info("Quit event detected during input wait")
                    waiting_for_input = False
                    running = False
                if event.type == pygame.KEYDOWN:
                    logging.debug(f"Key pressed: {event.key}")
                    if event.key == pygame.K_RETURN:
                        logging.info("Enter key pressed")
                        table.play_round()
                        waiting_for_input = False

        # table.reset_round()

    pygame.quit()
    logging.info("Game exited")

if __name__ == "__main__":
    main()