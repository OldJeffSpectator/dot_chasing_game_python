"""Visual representation of the game background."""
import pygame
from .base_pic import BasePic
from src.config.config_loader import config


class BackgroundPic(BasePic):
    """A black background matching screen dimensions."""
    
    def __init__(self):
        """Initialize the background visual properties."""
        cfg = config.get('media', 'pics', 'background_pic')
        # Get dimensions from screen config to avoid duplication
        self.width = config.get_screen_width()
        self.height = config.get_screen_height()
        self.color = tuple(cfg['color'])
    
    def draw(self, surface: pygame.Surface, x: float = 0, y: float = 0):
        """
        Draw the background on the given surface.
        
        Args:
            surface: The pygame Surface to draw on
            x: The x-coordinate (typically 0)
            y: The y-coordinate (typically 0)
        """
        surface.fill(self.color)
    
    def get_size(self) -> tuple[int, int]:
        """
        Get the size of the background.
        
        Returns:
            A tuple (width, height)
        """
        return (self.width, self.height)
