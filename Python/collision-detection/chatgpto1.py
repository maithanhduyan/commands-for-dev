import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Square with Bouncing Ball")

# Clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 60

# Define the square properties in LOCAL SPACE
# We'll make a square of side 400, so half_side = 200
half_side = 200

# Ball properties
ball_radius = 20
ball_speed = [3, 4]  # vx, vy in local space
ball_pos = [0, 0]    # x, y in local space

# Rotation angle of the square (and how much it changes per frame)
angle = 0.0
angle_speed = 0.5  # degrees per frame

# Helper function: rotate a point (x, y) in local space by "angle" degrees
# to get the coordinates in screen space, with the center of rotation
# set to the center of the screen.
def rotate_point_local_to_screen(x, y, angle_degs, center_x, center_y):
    # Convert degrees to radians
    angle_rads = math.radians(angle_degs)
    
    # Apply 2D rotation about origin (0,0) in local space
    x_rot = x * math.cos(angle_rads) - y * math.sin(angle_rads)
    y_rot = x * math.sin(angle_rads) + y * math.cos(angle_rads)
    
    # Translate so the center is at (center_x, center_y)
    x_screen = x_rot + center_x
    y_screen = y_rot + center_y
    
    return x_screen, y_screen

# Main loop
running = True
while running:
    clock.tick(FPS)
    
    # --- EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # --- UPDATE LOGIC ---

    # 1. Update ball position in local space
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]
    
    # 2. Collision detection in local space
    #    The square in local space has corners at:
    #        (-half_side, -half_side), (half_side, -half_side),
    #        (half_side, half_side),   (-half_side, half_side)
    #    We ensure the ball stays within these boundaries:
    #        x in [-half_side+ball_radius, half_side-ball_radius]
    #        y in [-half_side+ball_radius, half_side-ball_radius]
    if ball_pos[0] < -(half_side - ball_radius):
        ball_pos[0] = -(half_side - ball_radius)
        ball_speed[0] = -ball_speed[0]
    elif ball_pos[0] > (half_side - ball_radius):
        ball_pos[0] = (half_side - ball_radius)
        ball_speed[0] = -ball_speed[0]
    
    if ball_pos[1] < -(half_side - ball_radius):
        ball_pos[1] = -(half_side - ball_radius)
        ball_speed[1] = -ball_speed[1]
    elif ball_pos[1] > (half_side - ball_radius):
        ball_pos[1] = (half_side - ball_radius)
        ball_speed[1] = -ball_speed[1]
    
    # 3. Update the rotation angle
    angle += angle_speed
    angle %= 360  # keep angle between 0 and 359
    
    # --- RENDERING ---
    screen.fill((0, 0, 0))  # Clear screen with black
    
    # Draw the rotating square:
    #   We'll compute the four corners in local space, then rotate+translate them
    #   to screen coordinates.
    corners_local = [
        (-half_side, -half_side),
        ( half_side, -half_side),
        ( half_side,  half_side),
        (-half_side,  half_side)
    ]
    
    # Rotate each corner to screen coordinates
    square_points = []
    for (x_local, y_local) in corners_local:
        x_screen, y_screen = rotate_point_local_to_screen(
            x_local, y_local,
            angle,
            WIDTH // 2, HEIGHT // 2
        )
        square_points.append((x_screen, y_screen))
    
    # Use pygame to draw the polygon
    pygame.draw.polygon(screen, (100, 100, 255), square_points, width=2)
    
    # Now draw the ball
    #   Convert the ball's local position to screen coordinates
    ball_x_screen, ball_y_screen = rotate_point_local_to_screen(
        ball_pos[0], ball_pos[1],
        angle,
        WIDTH // 2,
        HEIGHT // 2
    )
    
    pygame.draw.circle(screen, (255, 255, 0), (int(ball_x_screen), int(ball_y_screen)), ball_radius)
    
    # Flip the display buffer
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
