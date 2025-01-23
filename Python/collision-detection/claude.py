import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball in Rotating Square")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Ball properties
ball_radius = 20
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = 5, 5

# Square properties
square_size = 400
square_angle = 0
rotation_speed = 0.5  # degrees per frame

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Rotate the square
    square_angle += rotation_speed
    
    # Calculate square vertices with rotation
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    half_size = square_size / 2
    
    # Rotated square vertices
    angle_rad = math.radians(square_angle)
    vertices = [
        (center_x + half_size * math.cos(angle_rad + math.pi/4), 
         center_y + half_size * math.sin(angle_rad + math.pi/4)),
        (center_x + half_size * math.cos(angle_rad + 3*math.pi/4), 
         center_y + half_size * math.sin(angle_rad + 3*math.pi/4)),
        (center_x + half_size * math.cos(angle_rad + 5*math.pi/4), 
         center_y + half_size * math.sin(angle_rad + 5*math.pi/4)),
        (center_x + half_size * math.cos(angle_rad + 7*math.pi/4), 
         center_y + half_size * math.sin(angle_rad + 7*math.pi/4))
    ]

    # Draw rotated square
    pygame.draw.polygon(screen, BLACK, vertices, 2)

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Collision detection with rotated square
    # Project ball center onto square's local coordinate system
    local_x = ball_x - center_x
    local_y = ball_y - center_y
    
    # Rotate local coordinates opposite to square rotation
    rot_x = local_x * math.cos(-angle_rad) - local_y * math.sin(-angle_rad)
    rot_y = local_x * math.sin(-angle_rad) + local_y * math.cos(-angle_rad)

    # Check if ball is outside the square's bounds
    if (abs(rot_x) > half_size - ball_radius or 
        abs(rot_y) > half_size - ball_radius):
        # Reverse velocities to bounce
        if abs(rot_x) > half_size - ball_radius:
            ball_speed_x *= -1
        if abs(rot_y) > half_size - ball_radius:
            ball_speed_y *= -1

    # Draw the ball
    pygame.draw.circle(screen, YELLOW, (int(ball_x), int(ball_y)), ball_radius)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()