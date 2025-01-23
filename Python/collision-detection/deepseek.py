# This code was created by Deepseek A.I with prompt: 
"""
This code was created by Deepseek A.I with prompt: 
write a python script for a bouncing yellow ball within a square, make sure to handle collision detection properly. 
make the square slowly rotate. 
implement it in python. make sure ball stays within the square


Create a game where a ball bounces inside a rotating square. 
The square should rotate around its center at a constant speed. 
The ball should bounce off the walls of the square. 
The ball should move at a constant speed
"""

import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball in Rotating Square")

# Colors
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Square parameters
SQUARE_CENTER = (WIDTH // 2, HEIGHT // 2)
SQUARE_SIZE = 200
SQUARE_HALF = SQUARE_SIZE // 2
ROTATION_SPEED = 0.5  # Degrees per frame

# Ball parameters
BALL_RADIUS = 20
BALL_SPEED = 5
ball_pos = [SQUARE_CENTER[0], SQUARE_CENTER[1] - SQUARE_HALF + BALL_RADIUS]
ball_vel = [BALL_SPEED, BALL_SPEED]

# Initialize clock
clock = pygame.time.Clock()

def rotate_point(x, y, angle):
    """Rotate a point (x, y) by given angle in degrees around origin"""
    rad = math.radians(angle)
    cos = math.cos(rad)
    sin = math.sin(rad)
    return x * cos - y * sin, x * sin + y * cos

running = True
angle = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update rotation angle
    angle = (angle + ROTATION_SPEED) % 360

    # Move ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Convert ball position to square's local coordinates
    dx = ball_pos[0] - SQUARE_CENTER[0]
    dy = ball_pos[1] - SQUARE_CENTER[1]
    rad = math.radians(angle)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)
    
    # Rotate ball position inversely to account for square's rotation
    local_x = dx * cos_a + dy * sin_a
    local_y = -dx * sin_a + dy * cos_a

    # Collision detection and response
    collision = False

    # Check left/right collisions
    if local_x - BALL_RADIUS < -SQUARE_HALF:
        collision = True
        normal = (cos_a, sin_a)  # Left wall normal
        local_x = -SQUARE_HALF + BALL_RADIUS
    elif local_x + BALL_RADIUS > SQUARE_HALF:
        collision = True
        normal = (-cos_a, -sin_a)  # Right wall normal
        local_x = SQUARE_HALF - BALL_RADIUS

    # Check top/bottom collisions
    if local_y - BALL_RADIUS < -SQUARE_HALF:
        collision = True
        normal = (-sin_a, cos_a)  # Top wall normal
        local_y = -SQUARE_HALF + BALL_RADIUS
    elif local_y + BALL_RADIUS > SQUARE_HALF:
        collision = True
        normal = (sin_a, -cos_a)  # Bottom wall normal
        local_y = SQUARE_HALF - BALL_RADIUS

    if collision:
        # Reflect velocity vector
        dot = ball_vel[0] * normal[0] + ball_vel[1] * normal[1]
        ball_vel[0] -= 2 * dot * normal[0]
        ball_vel[1] -= 2 * dot * normal[1]

        # Convert back to global coordinates
        ball_pos[0] = SQUARE_CENTER[0] + local_x * cos_a - local_y * sin_a
        ball_pos[1] = SQUARE_CENTER[1] + local_x * sin_a + local_y * cos_a

    # Drawing
    screen.fill(BLACK)

    # Draw rotating square
    corners = [
        (-SQUARE_HALF, -SQUARE_HALF),
        (SQUARE_HALF, -SQUARE_HALF),
        (SQUARE_HALF, SQUARE_HALF),
        (-SQUARE_HALF, SQUARE_HALF)
    ]
    rotated_corners = []
    for x, y in corners:
        rx, ry = rotate_point(x, y, angle)
        rotated_corners.append((SQUARE_CENTER[0] + rx, SQUARE_CENTER[1] + ry))
    pygame.draw.lines(screen, WHITE, True, rotated_corners, 2)

    # Draw ball
    pygame.draw.circle(screen, YELLOW, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()