"""Spawning logic for the white arrow."""
from src.general.position import Position


class WhiteArrowSpawn:
    """Handles spawning of the white arrow at game start."""
    
    def __init__(self, screen_width: int, screen_height: int):
        """
        Initialize the white arrow spawn logic.
        
        Args:
            screen_width: Width of the game screen
            screen_height: Height of the game screen
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.has_spawned = False
    
    def spawn(self) -> Position:
        """
        Spawn the white arrow at the center of the screen.
        
        This should only be called at the beginning of the game.
        
        Returns:
            A Position object for the white arrow
        """
        if not self.has_spawned:
            self.has_spawned = True
            return Position(self.screen_width / 2, self.screen_height / 2)
        return None
    
    def reset(self):
        """Reset the spawn state for a new game."""
        self.has_spawned = False
