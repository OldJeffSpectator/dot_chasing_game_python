"""Visual representation of a red dot."""
import pygame
from .base_pic import BasePic
from src.config.config_loader import config


class RedDotPic(BasePic):
    """A circular red dot with white boundary."""
    
    def __init__(self):
        """Initialize the red dot visual properties."""
        cfg = config.get('media', 'pics', 'red_dot_pic')
        self.diameter = cfg['diameter']
        self.radius = cfg['radius']
        self.color = tuple(cfg['color'])
        self.border_color = tuple(cfg['border_color'])
        self.border_width = cfg['border_width']
    
    def draw(self, surface: pygame.Surface, x: float, y: float):
        """
        Draw the red dot on the given surface.
        
        Args:
            surface: The pygame Surface to draw on
            x: The x-coordinate of the center
            y: The y-coordinate of the center
        """
        # Draw the red circle
        pygame.draw.circle(surface, self.color, (int(x), int(y)), self.radius)
        # Draw the white border
        pygame.draw.circle(surface, self.border_color, (int(x), int(y)), 
                         self.radius, self.border_width)
    
    def get_size(self) -> tuple[int, int]:
        """
        Get the size of the red dot.
        
        Returns:
            A tuple (width, height) = (diameter, diameter)
        """
        return (self.diameter, self.diameter)
