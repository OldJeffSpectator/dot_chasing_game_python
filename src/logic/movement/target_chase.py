"""Movement behavior that chases a target position."""
from src.general.position import Position
from .base_movement import BaseMovement


class TargetChase(BaseMovement):
    """Movement behavior that chases a target position."""
    
    def __init__(self, speed: float = 1.0):
        """
        Initialize the target chase movement.
        
        Args:
            speed: The movement speed in pixels per frame (should be provided by item)
        """
        super().__init__(speed)
    
    def update_position(self, current_position: Position, target_position: Position = None) -> Position:
        """
        Update position by moving towards the target.
        
        Args:
            current_position: The current position of the object
            target_position: The position to chase (e.g., white arrow position)
            
        Returns:
            The new position after moving towards the target
        """
        if target_position is None:
            return current_position
        
        # Calculate direction vector
        dx = target_position.x - current_position.x
        dy = target_position.y - current_position.y
        
        # Calculate distance
        distance = (dx ** 2 + dy ** 2) ** 0.5
        
        # If already at target, don't move
        if distance < 0.1:
            return current_position
        
        # Normalize direction and apply speed
        move_distance = min(self.speed, distance)
        dx = (dx / distance) * move_distance
        dy = (dy / distance) * move_distance
        
        # Return new position
        return Position(current_position.x + dx, current_position.y + dy)
