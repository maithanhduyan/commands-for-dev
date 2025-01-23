import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball in Rotating Square")

# Colors
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Ball properties
ball_radius = 10
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = 3, 3

# Square properties
square_size = 300
square_center = (WIDTH // 2, HEIGHT // 2)
square_angle = 0  # Initial rotation angle in degrees
rotation_speed = 1  # Rotation speed in degrees per frame

def rotate_point(point, center, angle):
    """Rotate a point around a center by a given angle."""
    x, y = point
    cx, cy = center
    radians = math.radians(angle)
    cos_theta = math.cos(radians)
    sin_theta = math.sin(radians)
    nx = cos_theta * (x - cx) - sin_theta * (y - cy) + cx
    ny = sin_theta * (x - cx) + cos_theta * (y - cy) + cy
    return nx, ny

def get_square_corners(center, size, angle):
    """Calculate the four corners of the rotated square."""
    cx, cy = center
    half_size = size / 2
    corners = [
        (cx - half_size, cy - half_size),
        (cx + half_size, cy - half_size),
        (cx + half_size, cy + half_size),
        (cx - half_size, cy + half_size),
    ]
    rotated_corners = [rotate_point(corner, center, angle) for corner in corners]
    return rotated_corners

def point_in_polygon(point, polygon):
    """Check if a point is inside a polygon using the ray-casting algorithm."""
    x, y = point
    n = len(polygon)
    inside = False

    px1, py1 = polygon[0]
    for i in range(n + 1):
        px2, py2 = polygon[i % n]
        if y > min(py1, py2):
            if y <= max(py1, py2):
                if x <= max(px1, px2):
                    if py1 != py2:
                        xinters = (y - py1) * (px2 - px1) / (py2 - py1) + px1
                    if px1 == px2 or x <= xinters:
                        inside = not inside
        px1, py1 = px2, py2

    return inside

def reflect_ball(ball_pos, ball_dir, square_corners):
    """Reflect the ball's direction when it hits the square edges."""
    bx, by = ball_pos
    dx, dy = ball_dir

    # Check each edge of the square for collision and reflect direction accordingly.
    for i in range(len(square_corners)):
        p1 = square_corners[i]
        p2 = square_corners[(i + 1) % len(square_corners)]

        # Edge vector and normal vector calculation.
        edge_vector = (p2[0] - p1[0], p2[1] - p1[1])
        edge_length_squared = edge_vector[0] ** 2 + edge_vector[1] ** 2

        # Project ball onto edge to find closest point.
        t = max(0, min(1,
                       ((bx - p1[0]) * edge_vector[0] + (by - p1[1]) * edge_vector[1]) / edge_length_squared))
        closest_point_x = p1[0] + t * edge_vector[0]
        closest_point_y = p1[1] + t * edge_vector[1]

        # Distance from ball to closest point on edge.
        dist_squared_to_edge = ((bx - closest_point_x) ** 2 +
                                (by - closest_point_y) ** 2)
