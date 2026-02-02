"""Base class for all visual representations."""
from abc import ABC, abstractmethod
import pygame


class BasePic(ABC):
    """Abstract base class for visual representations of game objects."""
    
    @abstractmethod
    def draw(self, surface: pygame.Surface, x: float, y: float):
        """
        Draw the visual representation on the given surface.
        
        Args:
            surface: The pygame Surface to draw on
            x: The x-coordinate to draw at
            y: The y-coordinate to draw at
        """
        pass
    
    @abstractmethod
    def get_size(self) -> tuple[int, int]:
        """
        Get the size of the visual representation.
        
        Returns:
            A tuple (width, height)
        """
        pass
