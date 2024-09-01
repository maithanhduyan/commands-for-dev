import pygame
import sys
import math
import tkinter as tk
from tkinter import messagebox

# Khởi tạo Pygame
pygame.init()

# Định nghĩa các màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Định nghĩa kích thước màn hình
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Định nghĩa màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(WHITE)

# Board
board = [[None, None, None], 
         [None, None, None], 
         [None, None, None]]

# Để theo dõi người chơi
player = 'X'
game_over = False

# Vẽ đường thẳng
def draw_lines():
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, BLACK, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Vẽ dấu X
def draw_cross(row, col):
    start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
    end_desc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
    pygame.draw.line(screen, RED, start_desc, end_desc, CROSS_WIDTH)
    start_asc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
    end_asc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
    pygame.draw.line(screen, RED, start_asc, end_asc, CROSS_WIDTH)

# Vẽ dấu O
def draw_circle(row, col):
    center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
    pygame.draw.circle(screen, BLACK, center, CIRCLE_RADIUS, CIRCLE_WIDTH)

# Vẽ lên bảng
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                draw_cross(row, col)
            elif board[row][col] == 'O':
                draw_circle(row, col)

# Kiểm tra chiến thắng
def check_win(player):
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Hiển thị hộp thoại thông báo
def display_message_box(message):
    root = tk.Tk()
    root.withdraw()  # Ẩn cửa sổ chính của tkinter
    messagebox.showinfo("Kết quả trò chơi", message)
    root.destroy()
    return

# Kiểm tra ô trống
def check_empty_cells():
    empty_cells = []
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                empty_cells.append((row, col))
    return empty_cells

# Kiểm tra hòa
def check_tie():
    if len(check_empty_cells()) == 0:
        return True
    return False

# Thuật toán Minimax
def minimax(board, depth, is_maximizing):
    if check_win('O'):
        return 1
    if check_win('X'):
        return -1
    if check_tie():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for cell in check_empty_cells():
            row, col = cell
            board[row][col] = 'O'
            score = minimax(board, depth + 1, False)
            board[row][col] = None
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for cell in check_empty_cells():
            row, col = cell
            board[row][col] = 'X'
            score = minimax(board, depth + 1, True)
            board[row][col] = None
            best_score = min(score, best_score)
        return best_score

# Lựa chọn nước đi tốt nhất
def best_move():
    best_score = -math.inf
    move = None
    for cell in check_empty_cells():
        row, col = cell
        board[row][col] = 'O'
        score = minimax(board, 0, False)
        board[row][col] = None
        if score > best_score:
            best_score = score
            move = (row, col)
    return move

# Reset bảng
def restart():
    screen.fill(WHITE)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = None

# Main loop
draw_lines()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] is None:
                board[clicked_row][clicked_col] = player
                draw_figures()
                pygame.display.update()  # Cập nhật màn hình ngay sau khi vẽ dấu X

                if check_win(player):
                    display_message_box(f"{player} thắng!")
                    restart()
                    player = 'X'
                    game_over = False
                elif check_tie():
                    display_message_box("Hòa!")
                    restart()
                    player = 'X'
                    game_over = False
                else:
                    player = 'O'
                    move = best_move()
                    if move:
                        board[move[0]][move[1]] = 'O'
                        draw_figures()
                        pygame.display.update()  # Cập nhật màn hình ngay sau khi vẽ dấu O
                        if check_win('O'):
                            display_message_box("O thắng!")
                            restart()
                            player = 'X'
                            game_over = False
                        elif check_tie():
                            display_message_box("Hòa!")
                            restart()
                            player = 'X'
                            game_over = False
                    player = 'X'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 'X'
                game_over = False

    pygame.display.update()
