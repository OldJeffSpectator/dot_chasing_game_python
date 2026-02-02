"""Base class for all game items."""
from abc import ABC, abstractmethod
import pygame
from src.general.position import Position
from src.media.pics.base_pic import BasePic
from src.logic.movement.base_movement import BaseMovement


class BaseItem(ABC):
    """Abstract base class for game items."""
    
    def __init__(self, position: Position, pic: BasePic, movement: BaseMovement, layer: int):
        """
        Initialize a game item.
        
        Args:
            position: The initial position of the item
            pic: The visual representation
            movement: The movement behavior
            layer: The rendering layer (0 = background, higher = foreground)
        """
        self.position = position
        self.pic = pic
        self.movement = movement
        self.layer = layer
    
    def update(self, **kwargs):
        """
        Update the item's state.
        
        Args:
            **kwargs: Parameters needed for the update (e.g., target_position)
        """
        if self.movement:
            self.position = self.movement.update_position(self.position, **kwargs)
    
    def draw(self, surface: pygame.Surface):
        """
        Draw the item on the given surface.
        
        Args:
            surface: The pygame Surface to draw on
        """
        if self.pic:
            self.pic.draw(surface, self.position.x, self.position.y)
