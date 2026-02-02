"""Collision detection between red dots and white arrow."""
from src.general.items.red_dot import RedDot
from src.general.items.white_arrow import WhiteArrow
from src.config.config_loader import config


class RedDotCollideWhiteArrow:
    """Detects collisions between red dots and the white arrow."""
    
    def __init__(self, red_dot_radius: float = None):
        """
        Initialize the collision detector.
        
        Args:
            red_dot_radius: Radius of red dots for collision (default: from red_dot_pic config)
        """
        if red_dot_radius is None:
            # Read radius from red_dot_pic config to avoid duplication
            red_dot_radius = config.get('media', 'pics', 'red_dot_pic', 'radius')
        self.red_dot_radius = red_dot_radius
    
    def check_collision(self, red_dot: RedDot, white_arrow: WhiteArrow) -> bool:
        """
        Check if a red dot collides with the white arrow.
        
        Args:
            red_dot: The red dot to check
            white_arrow: The white arrow to check
            
        Returns:
            True if collision detected, False otherwise
        """
        distance = red_dot.position.distance_to(white_arrow.position)
        return distance < self.red_dot_radius
    
    def check_all_collisions(self, red_dots: list, white_arrow: WhiteArrow) -> bool:
        """
        Check if any red dot collides with the white arrow.
        
        Args:
            red_dots: List of red dots to check
            white_arrow: The white arrow to check
            
        Returns:
            True if any collision detected, False otherwise
        """
        if white_arrow is None:
            return False
        
        for red_dot in red_dots:
            if self.check_collision(red_dot, white_arrow):
                return True
        return False
