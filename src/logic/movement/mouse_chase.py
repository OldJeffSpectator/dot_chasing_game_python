"""Movement behavior that chases the mouse position."""
import pygame
from src.general.position import Position
from .base_movement import BaseMovement


class MouseChase(BaseMovement):
    """Movement behavior that chases the real-time mouse position."""
    
    def __init__(self, speed: float = 1.0):
        """
        Initialize the mouse chase movement.
        
        Args:
            speed: The movement speed in pixels per frame (should be provided by item)
        """
        super().__init__(speed)
        self.last_dx = 0
        self.last_dy = 0
    
    def get_last_direction(self) -> tuple[float, float]:
        """
        Get the last movement direction.
        
        Returns:
            Tuple of (dx, dy)
        """
        return (self.last_dx, self.last_dy)
    
    def update_position(self, current_position: Position, **kwargs) -> Position:
        """
        Update position by moving towards the mouse cursor.
        
        Args:
            current_position: The current position of the object
            **kwargs: Additional parameters (not used)
            
        Returns:
            The new position after moving towards the mouse
        """
        # Get current mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_position = Position(mouse_x, mouse_y)
        
        # Calculate direction vector
        dx = mouse_position.x - current_position.x
        dy = mouse_position.y - current_position.y
        
        # Calculate distance
        distance = (dx ** 2 + dy ** 2) ** 0.5
        
        # If already at mouse position, don't move
        if distance < 0.1:
            return current_position
        
        # Normalize direction and apply speed
        move_distance = min(self.speed, distance)
        dx = (dx / distance) * move_distance
        dy = (dy / distance) * move_distance
        
        # Store last direction for rotation
        self.last_dx = dx
        self.last_dy = dy
        
        # Return new position
        return Position(current_position.x + dx, current_position.y + dy)
