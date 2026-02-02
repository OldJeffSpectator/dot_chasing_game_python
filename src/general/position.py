"""Position class to define the location of game objects."""


class Position:
    """Represents a 2D position with x and y coordinates."""
    
    def __init__(self, x: float = 0, y: float = 0):
        """
        Initialize a position.
        
        Args:
            x: The x-coordinate
            y: The y-coordinate
        """
        self.x = x
        self.y = y
    
    def distance_to(self, other: 'Position') -> float:
        """
        Calculate the Euclidean distance to another position.
        
        Args:
            other: Another Position object
            
        Returns:
            The distance between this position and the other
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
    def copy(self) -> 'Position':
        """Return a copy of this position."""
        return Position(self.x, self.y)
    
    def __repr__(self):
        return f"Position(x={self.x}, y={self.y})"
