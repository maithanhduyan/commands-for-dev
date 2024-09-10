import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Các thông số cơ bản của game
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# Các hình dạng khối Tetris
SHAPES = {
    'I': [[1, 1, 1, 1]],
    'J': [[1, 0, 0], [1, 1, 1]],
    'L': [[0, 0, 1], [1, 1, 1]],
    'O': [[1, 1], [1, 1]],
    'S': [[0, 1, 1], [1, 1, 0]],
    'T': [[0, 1, 0], [1, 1, 1]],
    'Z': [[1, 1, 0], [0, 1, 1]],
}

# Màu sắc khối Tetris
COLORS = {
    'I': (0, 255, 255),
    'J': (0, 0, 255),
    'L': (255, 165, 0),
    'O': (255, 255, 0),
    'S': (0, 255, 0),
    'T': (128, 0, 128),
    'Z': (255, 0, 0),
}

# Lớp Tetris
class Tetris:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_shape = self.get_new_shape()
        self.next_shape = self.get_new_shape()
        self.score = 0
        self.game_over = False

    def get_new_shape(self):
        shape_type = random.choice(list(SHAPES.keys()))
        shape = SHAPES[shape_type]
        color = COLORS[shape_type]
        return {'shape': shape, 'color': color, 'x': GRID_WIDTH // 2 - len(shape[0]) // 2, 'y': 0}

    def draw_grid(self, screen):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y][x]:
                    pygame.draw.rect(screen, self.grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def draw_shape(self, screen, shape, offset_x, offset_y):
        for y, row in enumerate(shape['shape']):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, shape['color'], 
                                     ((shape['x'] + x + offset_x) * BLOCK_SIZE, 
                                      (shape['y'] + y + offset_y) * BLOCK_SIZE, 
                                      BLOCK_SIZE, BLOCK_SIZE))

    def move_shape(self, dx, dy):
        self.current_shape['x'] += dx
        self.current_shape['y'] += dy

    def rotate_shape(self):
        shape = self.current_shape['shape']
        self.current_shape['shape'] = [list(row) for row in zip(*shape[::-1])]

    def check_collision(self):
        shape = self.current_shape['shape']
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    if (self.current_shape['y'] + y >= GRID_HEIGHT or
                        self.current_shape['x'] + x >= GRID_WIDTH or
                        self.current_shape['x'] + x < 0 or
                        self.grid[self.current_shape['y'] + y][self.current_shape['x'] + x]):
                        return True
        return False

    def lock_shape(self):
        shape = self.current_shape['shape']
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    grid_y = self.current_shape['y'] + y
                    grid_x = self.current_shape['x'] + x
                    if 0 <= grid_y < GRID_HEIGHT and 0 <= grid_x < GRID_WIDTH:
                        self.grid[grid_y][grid_x] = self.current_shape['color']
        self.clear_lines()
        self.current_shape = self.next_shape
        self.next_shape = self.get_new_shape()
        if self.check_collision():
            self.game_over = True

    def clear_lines(self):
        lines_cleared = 0
        for y in range(GRID_HEIGHT):
            if all(self.grid[y]):
                del self.grid[y]
                self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])
                lines_cleared += 1
        self.score += lines_cleared * 100

    def update(self):
        self.move_shape(0, 1)
        if self.check_collision():
            self.move_shape(0, -1)
            self.lock_shape()

    def ai_move(self):
        # Đơn giản hóa AI bằng cách di chuyển khối ngẫu nhiên hoặc theo một quy tắc nào đó
        best_move = random.choice(['left', 'right', 'rotate'])
        if best_move == 'left':
            self.move_shape(-1, 0)
        elif best_move == 'right':
            self.move_shape(1, 0)
        elif best_move == 'rotate':
            self.rotate_shape()
        self.update()

# Chạy game
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris AI")
    clock = pygame.time.Clock()
    game = Tetris()

    running = True
    while running:
        screen.fill((0, 0, 0))
        game.draw_grid(screen)
        game.draw_shape(screen, game.current_shape, 0, 0)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.update()
        game.ai_move()

        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
