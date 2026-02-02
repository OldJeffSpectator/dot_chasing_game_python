"""Spawning logic for green circles (bomb waves)."""
from src.general.position import Position


class GreenCircleSpawn:
    """Handles spawning of green circles at specified positions."""
    
    def __init__(self):
        """Initialize the green circle spawn logic."""
        pass
    
    def spawn(self, spawn_position: Position) -> Position:
        """
        Spawn a green circle at the specified position.
        
        Args:
            spawn_position: Position where the green circle should spawn
            
        Returns:
            A copy of the spawn position
        """
        return spawn_position.copy()
