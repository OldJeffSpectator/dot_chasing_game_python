"""Spawning logic for red dots."""
import random
from src.general.position import Position
from src.config.config_loader import config


class RedDotSpawn:
    """Handles spawning of red dots at random locations."""
    
    def __init__(self, screen_width: int, screen_height: int, min_distance: float = None):
        """
        Initialize the red dot spawn logic.
        
        Args:
            screen_width: Width of the game screen
            screen_height: Height of the game screen
            min_distance: Minimum distance from white arrow position (default: from config)
        """
        cfg = config.get('logic', 'item_spawn', 'red_dot_spawn')
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.min_distance = min_distance if min_distance is not None else cfg['min_distance_from_arrow']
        self.max_attempts = cfg['max_spawn_attempts']
        self.margin = cfg['margin']
    
    def spawn(self, avoid_position: Position = None) -> Position:
        """
        Spawn a red dot at a random location.
        
        Args:
            avoid_position: Position to avoid (e.g., white arrow position)
            
        Returns:
            A Position object for the new red dot
        """
        for _ in range(self.max_attempts):
            # Generate random position within screen bounds
            x = random.uniform(self.margin, self.screen_width - self.margin)
            y = random.uniform(self.margin, self.screen_height - self.margin)
            new_position = Position(x, y)
            
            # If no position to avoid, return this position
            if avoid_position is None:
                return new_position
            
            # Check if far enough from the avoid position
            distance = new_position.distance_to(avoid_position)
            if distance >= self.min_distance:
                return new_position
        
        # If we couldn't find a valid position after max_attempts,
        # just return a random position anyway
        return Position(
            random.uniform(self.margin, self.screen_width - self.margin),
            random.uniform(self.margin, self.screen_height - self.margin)
        )
