# game/snake/snake_game.py

import pygame
import random

# ---------------------------
# Các lớp hướng đối tượng
# ---------------------------

class Food:
    """
    Đại diện cho thức ăn trong game Snake.
    """
    def __init__(self, grid_width, grid_height, snake_body):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.position = self.random_position(snake_body)

    def random_position(self, snake_body):
        """
        Đặt thức ăn ở vị trí ngẫu nhiên mà không trùng với thân rắn.
        """
        while True:
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            if (x, y) not in snake_body:
                return (x, y)

    def reset(self, snake_body):
        """
        Thay đổi vị trí thức ăn (khi bị ăn).
        """
        self.position = self.random_position(snake_body)


class Snake:
    """
    Đại diện cho rắn: đầu rắn + danh sách thân (các ô).
    Hướng di chuyển (dx, dy).
    """
    def __init__(self, x, y):
        # Khởi tạo thân rắn: 1 segment
        self.body = [(x, y)]
        # Hướng mặc định: đi lên
        self.direction = (0, -1)
        self.score = 0

    def turn_left(self):
        dx, dy = self.direction
        # up (0,-1) -> left (-1,0)
        self.direction = (-dy, dx)

    def turn_right(self):
        dx, dy = self.direction
        # up (0,-1) -> right (1,0)
        self.direction = (dy, -dx)

    def move_straight(self):
        # Giữ nguyên hướng
        pass

    def move(self):
        """
        Di chuyển rắn 1 bước. Trả về (new_x, new_y) là vị trí đầu mới.
        """
        dx, dy = self.direction
        head_x, head_y = self.body[0]
        new_x = head_x + dx
        new_y = head_y + dy
        # Thêm đầu mới vào body
        self.body.insert(0, (new_x, new_y))
        return new_x, new_y

    def grow(self):
        """
        Khi ăn thức ăn, rắn sẽ không xóa đuôi => tăng chiều dài.
        """
        # Không pop đuôi => rắn dài thêm 1
        pass

    def shrink_tail(self):
        """
        Xóa đuôi (nếu không ăn).
        """
        self.body.pop()


class SnakeGame:
    """
    Lớp quản lý game Snake (màn hình pygame, logic va chạm, vẽ...).
    """
    def __init__(self, width=20, height=20, cell_size=20, max_steps=400, fps=15):
        pygame.init()

        self.width = width             # số ô ngang
        self.height = height           # số ô dọc
        self.cell_size = cell_size     # kích thước mỗi ô (pixel)
        self.max_steps = max_steps     # giới hạn bước di chuyển
        self.fps = fps

        self.screen = pygame.display.set_mode(
            (self.width * self.cell_size, self.height * self.cell_size)
        )
        pygame.display.set_caption("Snake NEAT")

        self.clock = pygame.time.Clock()

        # Reset game
        self.reset()

    def reset(self):
        # Vị trí khởi tạo rắn (giữa màn hình)
        start_x = self.width // 2
        start_y = self.height // 2

        self.snake = Snake(start_x, start_y)
        self.food = Food(self.width, self.height, self.snake.body)

        self.steps = 0
        self.done = False

    def get_state(self):
        """
        Lấy thông tin môi trường để cung cấp cho AI:
        Ở đây ví dụ 4 features: khoảng cách food, hướng snake
        """
        (food_x, food_y) = self.food.position
        (head_x, head_y) = self.snake.body[0]
        dist_food_x = (food_x - head_x) / self.width
        dist_food_y = (food_y - head_y) / self.height
        dir_x, dir_y = self.snake.direction

        return [
            dist_food_x,
            dist_food_y,
            dir_x,
            dir_y
        ]

    def step(self, action):
        """
        action = 0 (turn left), 1 (straight), 2 (turn right)
        Di chuyển rắn, kiểm tra va chạm, tính reward.
        """
        if action == 0:
            self.snake.turn_left()
        elif action == 2:
            self.snake.turn_right()
        else:
            self.snake.move_straight()

        # Di chuyển rắn
        new_x, new_y = self.snake.move()

        # Kiểm tra va tường
        if not (0 <= new_x < self.width and 0 <= new_y < self.height):
            self.done = True
            return -10, True

        # Kiểm tra va thân
        if (new_x, new_y) in self.snake.body[1:]:
            self.done = True
            return -10, True

        reward = 0
        # Kiểm tra ăn
        if (new_x, new_y) == self.food.position:
            self.snake.score += 1
            reward = 10
            self.snake.grow()  # không pop đuôi => dài thêm
            self.food.reset(self.snake.body)
        else:
            self.snake.shrink_tail()
            reward = -0.5  # mỗi bước không ăn => phạt nhẹ

        self.steps += 1
        if self.steps >= self.max_steps:
            self.done = True

        return reward, self.done

    def render(self):
        self.screen.fill((0, 0, 0))

        # Vẽ thức ăn
        food_x, food_y = self.food.position
        pygame.draw.rect(
            self.screen,
            (255, 0, 0),
            pygame.Rect(
                food_x * self.cell_size,
                food_y * self.cell_size,
                self.cell_size,
                self.cell_size
            )
        )

        # Vẽ rắn
        for (sx, sy) in self.snake.body:
            pygame.draw.rect(
                self.screen,
                (0, 255, 0),
                pygame.Rect(
                    sx * self.cell_size,
                    sy * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
            )

        pygame.display.set_caption(f"Snake NEAT | Score: {self.snake.score}")
        pygame.display.flip()
        self.clock.tick(self.fps)

    def close(self):
        pygame.quit()
