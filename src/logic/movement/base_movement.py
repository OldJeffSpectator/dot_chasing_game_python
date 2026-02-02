"""Base class for all movement behaviors."""
from abc import ABC, abstractmethod
from src.general.position import Position


class BaseMovement(ABC):
    """Abstract base class for movement behaviors."""
    
    def __init__(self, speed: float):
        """
        Initialize the movement behavior.
        
        Args:
            speed: The movement speed in pixels per frame
        """
        self.speed = speed
    
    @abstractmethod
    def update_position(self, current_position: Position, **kwargs) -> Position:
        """
        Update the position based on the movement behavior.
        
        Args:
            current_position: The current position of the object
            **kwargs: Additional parameters specific to the movement type
            
        Returns:
            The new position after applying movement
        """
        pass
