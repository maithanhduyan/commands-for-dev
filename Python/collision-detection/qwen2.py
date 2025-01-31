# Qwen2.5-Max


import pygame
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball in Rotating Square")

# Colors
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Square properties
square_size = 400
square_center = (WIDTH // 2, HEIGHT // 2)
rotation_angle = 0  # Initial rotation angle
rotation_speed = 0.5  # Degrees per frame

# Ball properties
ball_radius = 15
ball_pos = [square_center[0] - square_size // 4, square_center[1]]  # Start inside the square
ball_velocity = [3, 2]  # Initial velocity

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Function to rotate a point around a center
def rotate_point(point, center, angle):
    angle_rad = math.radians(angle)
    px, py = point
    cx, cy = center
    x = cx + math.cos(angle_rad) * (px - cx) - math.sin(angle_rad) * (py - cy)
    y = cy + math.sin(angle_rad) * (px - cx) + math.cos(angle_rad) * (py - cy)
    return x, y

# Function to check if a point is inside the square
def is_inside_square(point, square_center, size, angle):
    # Transform the point to the square's local coordinate system
    rotated_point = rotate_point(point, square_center, -angle)
    cx, cy = square_center
    half_size = size / 2
    x, y = rotated_point
    return (cx - half_size <= x <= cx + half_size) and (cy - half_size <= y <= cy + half_size)

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update rotation angle
    rotation_angle += rotation_speed
    if rotation_angle >= 360:
        rotation_angle -= 360

    # Update ball position
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Check collision with the square
    if not is_inside_square(ball_pos, square_center, square_size, rotation_angle):
        # Reflect the velocity vector when the ball hits the square boundary
        ball_velocity[0] = -ball_velocity[0]
        ball_velocity[1] = -ball_velocity[1]

    # Draw the square
    points = [
        rotate_point((square_center[0] - square_size // 2, square_center[1] - square_size // 2), square_center, rotation_angle),
        rotate_point((square_center[0] + square_size // 2, square_center[1] - square_size // 2), square_center, rotation_angle),
        rotate_point((square_center[0] + square_size // 2, square_center[1] + square_size // 2), square_center, rotation_angle),
        rotate_point((square_center[0] - square_size // 2, square_center[1] + square_size // 2), square_center, rotation_angle),
    ]
    pygame.draw.polygon(screen, WHITE, points, 2)

    # Draw the ball
    pygame.draw.circle(screen, YELLOW, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()