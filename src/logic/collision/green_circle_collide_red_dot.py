"""Collision detection between green circles and red dots."""
from src.general.items.red_dot import RedDot
from src.general.items.green_circle import GreenCircle


class GreenCircleCollideRedDot:
    """Detects collisions between green circles and red dots."""
    
    def __init__(self):
        """Initialize the collision detector."""
        pass
    
    def check_collision(self, green_circle: GreenCircle, red_dot: RedDot) -> bool:
        """
        Check if a green circle collides with a red dot.
        
        Args:
            green_circle: The green circle to check
            red_dot: The red dot to check
            
        Returns:
            True if collision detected, False otherwise
        """
        distance = green_circle.position.distance_to(red_dot.position)
        return distance < green_circle.get_radius()
    
    def check_all_collisions(self, green_circles: list, red_dots: list) -> list:
        """
        Check collisions between all green circles and red dots.
        
        Args:
            green_circles: List of green circles
            red_dots: List of red dots
            
        Returns:
            List of red dots that should be destroyed
        """
        red_dots_to_destroy = []
        
        for green_circle in green_circles:
            for red_dot in red_dots:
                if red_dot not in red_dots_to_destroy:
                    if self.check_collision(green_circle, red_dot):
                        red_dots_to_destroy.append(red_dot)
        
        return red_dots_to_destroy
