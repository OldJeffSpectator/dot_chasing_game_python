"""Visual representation of a white arrow."""
import pygame
import math
from .base_pic import BasePic
from src.config.config_loader import config


class WhiteArrowPic(BasePic):
    """An arrow-shaped object that fits in a 15x13 pixel space."""
    
    def __init__(self):
        """Initialize the white arrow visual properties."""
        cfg = config.get('media', 'pics', 'white_arrow_pic')
        self.width = cfg['width']
        self.height = cfg['height']
        self.color = tuple(cfg['color'])
        self.rotation_angle = 0  # Angle in degrees (0 = pointing up)
    
    def set_rotation_from_direction(self, dx: float, dy: float):
        """
        Set the rotation angle based on movement direction.
        
        Args:
            dx: Change in x position
            dy: Change in y position
        """
        if abs(dx) > 0.1 or abs(dy) > 0.1:
            # Calculate angle in radians, then convert to degrees
            # atan2 returns angle from positive x-axis, we adjust for up-pointing arrow
            self.rotation_angle = math.degrees(math.atan2(dx, -dy))
    
    def draw(self, surface: pygame.Surface, x: float, y: float):
        """
        Draw the white arrow on the given surface.
        
        Args:
            surface: The pygame Surface to draw on
            x: The x-coordinate of the center
            y: The y-coordinate of the center
        """
        # Define arrow points (pointing up by default)
        # Arrow shape: tip at top, wings on sides, base at bottom
        half_width = self.width / 2
        half_height = self.height / 2
        
        # Points relative to origin (0, 0)
        points = [
            (0, -half_height),  # Top tip
            (half_width, half_height / 2),  # Right wing
            (half_width / 3, half_height / 2),  # Right inner
            (half_width / 3, half_height),  # Right base
            (-half_width / 3, half_height),  # Left base
            (-half_width / 3, half_height / 2),  # Left inner
            (-half_width, half_height / 2),  # Left wing
        ]
        
        # Rotate points
        angle_rad = math.radians(self.rotation_angle)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        
        rotated_points = []
        for px, py in points:
            # Rotate around origin
            rotated_x = px * cos_a - py * sin_a
            rotated_y = px * sin_a + py * cos_a
            # Translate to position
            rotated_points.append((x + rotated_x, y + rotated_y))
        
        pygame.draw.polygon(surface, self.color, rotated_points)
    
    def get_size(self) -> tuple[int, int]:
        """
        Get the size of the white arrow.
        
        Returns:
            A tuple (width, height)
        """
        return (self.width, self.height)
