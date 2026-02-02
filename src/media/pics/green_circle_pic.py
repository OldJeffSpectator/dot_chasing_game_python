"""Visual representation of a green circle (bomb wave)."""
import pygame
from .base_pic import BasePic
from src.config.config_loader import config


class GreenCirclePic(BasePic):
    """A circular green wave that expands from the bomb."""
    
    def __init__(self):
        """Initialize the green circle visual properties."""
        cfg = config.get('media', 'pics', 'green_circle_pic')
        self.base_radius = cfg['base_radius']
        self.max_radius = cfg['max_radius']
        self.current_radius = self.base_radius
        self.color = tuple(cfg['color'])
        self.alpha = cfg['alpha']
        self.border_width = cfg['border_width']
    
    def set_radius(self, progress: float):
        """
        Set the current radius based on animation progress.
        
        Args:
            progress: Progress from 0.0 to 1.0
        """
        self.current_radius = self.base_radius + (self.max_radius - self.base_radius) * progress
        # Fade out as it expands
        self.alpha = int(180 * (1 - progress))
    
    def draw(self, surface: pygame.Surface, x: float, y: float):
        """
        Draw the green circle on the given surface.
        
        Args:
            surface: The pygame Surface to draw on
            x: The x-coordinate of the center
            y: The y-coordinate of the center
        """
        # Create a transparent surface for the circle
        temp_surface = pygame.Surface((int(self.current_radius * 2), int(self.current_radius * 2)), pygame.SRCALPHA)
        pygame.draw.circle(temp_surface, (*self.color, self.alpha), 
                         (int(self.current_radius), int(self.current_radius)), 
                         int(self.current_radius))
        # Draw border
        pygame.draw.circle(temp_surface, (*self.color, 255), 
                         (int(self.current_radius), int(self.current_radius)), 
                         int(self.current_radius), self.border_width)
        
        # Blit to main surface
        surface.blit(temp_surface, (x - self.current_radius, y - self.current_radius))
    
    def get_size(self) -> tuple[int, int]:
        """
        Get the size of the green circle.
        
        Returns:
            A tuple (width, height) based on current radius
        """
        diameter = int(self.current_radius * 2)
        return (diameter, diameter)
    
    def get_radius(self) -> float:
        """
        Get the current radius of the circle.
        
        Returns:
            The current radius
        """
        return self.current_radius
