"""
This code was created by  XAI Grok2 with prompt:

write a python script for a bouncing yellow ball within a square, make sure to handle collision detection properly. make the square slowly rotate. implement it in python. make sure ball stays within the square
"""

import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
BALL_COLOR = (255, 255, 0)  # Yellow
SQUARE_SIZE = 300
SQUARE_COLOR = (0, 0, 255)  # Blue
BACKGROUND_COLOR = (0, 0, 0)  # Black
FPS = 60
ROTATION_SPEED = 0.5  # degrees per frame

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball in Rotating Square")

# Ball properties
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [5, 3]  # dx, dy

# Square properties
square_center = [WIDTH // 2, HEIGHT // 2]
square_rotation = 0

clock = pygame.time.Clock()

def rotate_point(point, angle, center):
    """Rotate a point around a center."""
    angle = math.radians(angle)
    x = point[0] - center[0]
    y = point[1] - center[1]
    new_x = x * math.cos(angle) - y * math.sin(angle)
    new_y = x * math.sin(angle) + y * math.cos(angle)
    return [new_x + center[0], new_y + center[1]]

def get_square_vertices(center, size, angle):
    """Get vertices of the square after rotation."""
    half_size = size // 2
    vertices = [
        rotate_point([center[0] - half_size, center[1] - half_size], angle, center),
        rotate_point([center[0] + half_size, center[1] - half_size], angle, center),
        rotate_point([center[0] + half_size, center[1] + half_size], angle, center),
        rotate_point([center[0] - half_size, center[1] + half_size], angle, center)
    ]
    return vertices

def ball_in_square(ball, vertices):
    """Check if ball center is inside the square."""
    px, py = ball.center
    count = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]
        if ((y1 > py) != (y2 > py)) and (px < (x2 - x1) * (py - y1) / (y2 - y1) + x1):
            count += 1
    return count % 2 == 1

def handle_collision(ball, vertices):
    """Handle ball collision with square's edges."""
    for i in range(len(vertices)):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % len(vertices)]
        closest_point = closest_point_on_line(v1, v2, ball.center)
        distance = math.dist(ball.center, closest_point)
        if distance <= BALL_RADIUS:
            normal = [v2[1] - v1[1], v1[0] - v2[0]]  # Perpendicular to line
            normal_length = math.sqrt(normal[0]**2 + normal[1]**2)
            if normal_length != 0:
                normal = [x / normal_length for x in normal]
                dot_product = ball_speed[0] * normal[0] + ball_speed[1] * normal[1]
                ball_speed[0] -= 2 * dot_product * normal[0]
                ball_speed[1] -= 2 * dot_product * normal[1]

def closest_point_on_line(start, end, point):
    """Find closest point on line segment to point."""
    line_vec = [end[0] - start[0], end[1] - start[1]]
    point_vec = [point[0] - start[0], point[1] - start[1]]
    line_length = line_vec[0]**2 + line_vec[1]**2
    if line_length == 0:
        return start
    t = max(0, min(1, (point_vec[0] * line_vec[0] + point_vec[1] * line_vec[1]) / line_length))
    return [start[0] + t * line_vec[0], start[1] + t * line_vec[1]]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Rotate square
    square_rotation += ROTATION_SPEED
    if square_rotation >= 360:
        square_rotation -= 360

    # Get square vertices after rotation
    vertices = get_square_vertices(square_center, SQUARE_SIZE, square_rotation)

    # Move ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Check if ball is outside the square or collides with edges
    if not ball_in_square(ball, vertices):
        handle_collision(ball, vertices)
    
    # Draw square
    pygame.draw.polygon(screen, SQUARE_COLOR, vertices, 2)

    # Draw ball
    pygame.draw.circle(screen, BALL_COLOR, ball.center, BALL_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()