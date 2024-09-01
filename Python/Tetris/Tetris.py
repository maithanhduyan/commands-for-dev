import pygame
import random
import logging
import sqlite3

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
grid_size = 30  # Kích thước mỗi ô lưới
columns = 10  # Số ô ngang
rows = 20  # Số ô dọc
screen_width = columns * grid_size
screen_height = rows * grid_size
screen = pygame.display.set_mode((screen_width, screen_height))

# Thiết lập tên game
pygame.display.set_caption("Tetris Drag and Drop")

# Màu sắc
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

rows = screen_height // grid_size
columns = screen_width // grid_size

# FPS (Frames Per Second)
clock = pygame.time.Clock()
fps = 30

# Drop speed
drop_speed = 300  # milliseconds

# Các hình dạng Tetris
shapes = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1], [1, 1]],  # O
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]]   # S
]

class TetrisBlock:
    def __init__(self):
        self.shape = random.choice(shapes)
        self.color = blue
        self.size = len(self.shape)
        self.x = screen_width // 2 // grid_size * grid_size
        self.y = 0
        self.dragging = False

    def draw(self, screen):
        for i, row in enumerate(self.shape):
            for j, value in enumerate(row):
                if value:
                    pygame.draw.rect(screen, self.color,
                                     (self.x + j * grid_size, self.y + i * grid_size, grid_size, grid_size))

    def rotate(self):
        # Rotate the shape 90 degrees to the right
        self.shape = [list(row) for row in zip(*self.shape[::-1])]
        # Check for collision after rotation
        if check_collision(self, self.x, self.y):
            # If collision occurs, rotate back
            self.shape = [list(row) for row in zip(*self.shape)]
    
# Initialize the grid
grid = [[0 for _ in range(columns)] for _ in range(rows)]

def check_collision(block, x, y):
    for i, row in enumerate(block.shape):
        for j, value in enumerate(row):
            if value:
                if y + i * grid_size >= screen_height or x + j * grid_size < 0 or x + j * grid_size >= screen_width:
                    return True
                if grid[(y + i * grid_size) // grid_size][(x + j * grid_size) // grid_size]:
                    return True
    return False

def place_block(block):
    global game_over  # Add this line
    for i, row in enumerate(block.shape):
        for j, value in enumerate(row):
            if value:
                grid_y = (block.y + i * grid_size) // grid_size
                grid_x = (block.x + j * grid_size) // grid_size
                grid[grid_y][grid_x] = 1
                if grid_y == 0:  # Check if the block is placed in the top row
                    game_over = True  # Set game_over flag to True
    check_complete_rows()  # Check for complete rows after placing a block

def drop_block(block):
    block.y += grid_size
    if check_collision(block, block.x, block.y):
        block.y -= grid_size
        place_block(block)
        return True
    return False

def handle_drag(block, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if block.x <= event.pos[0] < block.x + block.size * grid_size and block.y <= event.pos[1] < block.y + block.size * grid_size:
            block.dragging = True
    elif event.type == pygame.MOUSEBUTTONUP:
        block.dragging = False
    elif event.type == pygame.MOUSEMOTION:
        if block.dragging:
            block.x = event.pos[0] - grid_size
            block.y = event.pos[1] - grid_size


def draw_grid(screen):
    for y in range(rows):
        for x in range(columns):
            if grid[y][x]:
                pygame.draw.rect(screen, blue, (x * grid_size, y * grid_size, grid_size, grid_size))
            pygame.draw.rect(screen, white, (x * grid_size, y * grid_size, grid_size, grid_size), 1)  # Vẽ lưới

def move_block(block, dx):
    new_x = block.x + dx * grid_size
    if not check_collision(block, new_x, block.y):
        block.x = new_x

def draw_button(screen, text, x, y, width, height, color, hover_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))

    font = pygame.font.Font(None, 36)
    text_surf = font.render(text, True, black)
    text_rect = text_surf.get_rect(center=((x + (width / 2)), (y + (height / 2))))
    screen.blit(text_surf, text_rect)

def restart_game():
    global grid, current_block, game_over, last_drop_time, score
    grid = [[0 for _ in range(columns)] for _ in range(rows)]
    current_block = TetrisBlock()
    game_over = False
    last_drop_time = pygame.time.get_ticks()
    score = 0  # Reset score to 0

def check_complete_rows():
    global score
    complete_rows = 0
    for y in range(rows):
        if all(grid[y]):
            complete_rows += 1
            del grid[y]
            grid.insert(0, [0 for _ in range(columns)])
    score += complete_rows

def draw_score(screen):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, white)
    screen.blit(text, (10, 10))
    # Display the highest score
    high_score_text = font.render(f"High Score: {highest_score}", True, white)
    screen.blit(high_score_text, (10, 50))

# Tạo kết nối đến cơ sở dữ liệu SQLite
conn = sqlite3.connect('tetris_highscore.db')
c = conn.cursor()

# Tạo bảng nếu chưa tồn tại
c.execute('''CREATE TABLE IF NOT EXISTS highscore (score INTEGER)''')
conn.commit()

def get_highest_score():
    c.execute('SELECT MAX(score) FROM highscore')
    result = c.fetchone()
    return result[0] if result[0] is not None else 0

def save_highest_score(score):
    c.execute('INSERT INTO highscore (score) VALUES (?)', (score,))
    conn.commit()

def main():
    logging.info("Game started")
    running = True 
    global current_block, game_over, last_drop_time, score, highest_score
    current_block = TetrisBlock()
    last_drop_time = pygame.time.get_ticks()
    fast_drop = False
    game_over = False  # Initialize game_over flag
    score = 0  # Initialize score
    highest_score = get_highest_score()  # Get the highest score from the database

    while running:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    logging.info("K_BACKSPACE")
                elif event.key == pygame.K_LEFT:
                    logging.info("K_LEFT")
                    move_block(current_block, -1)
                elif event.key == pygame.K_RIGHT:
                    logging.info("K_RIGHT")
                    move_block(current_block, 1)
                elif event.key == pygame.K_DOWN:
                    logging.info("K_DOWN") 
                    drop_block(current_block)
                elif event.key == pygame.K_UP:
                    logging.info("K_UP")
                    current_block.rotate()
            
            handle_drag(current_block, event)

        current_time = pygame.time.get_ticks()

        if not game_over:  # Add this condition
            if not current_block.dragging and current_time - last_drop_time > drop_speed:
                if drop_block(current_block):
                    current_block = TetrisBlock()
                last_drop_time = current_time

            draw_grid(screen)
            current_block.draw(screen)
            draw_score(screen)  # Draw the score on the screen
        else:
            # Update the highest score if the current score is higher
            if score > highest_score:
                highest_score = score
                save_highest_score(score)  # Save the new highest score to the database

            # Display game over message and restart button
            font = pygame.font.Font(None, 58)
            text = font.render("Game Over", True, white)
            screen.blit(text, (screen_width // 4, screen_height // 2 - 50))
            draw_button(screen, "Restart", screen_width // 4, screen_height // 2 + 50, 200, 50, white, blue, restart_game)

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
    conn.close()  # Đóng kết nối cơ sở dữ liệu khi thoát game

if __name__ == "__main__":
    main()