"""Green circle game item (bomb wave)."""
from src.general.position import Position
from src.media.pics.green_circle_pic import GreenCirclePic
from src.config.config_loader import config
from .base_item import BaseItem


class GreenCircle(BaseItem):
    """A green circular wave that destroys red dots."""
    
    def __init__(self, position: Position, lifetime_frames: int = None):
        """
        Initialize a green circle.
        
        Args:
            position: The position where the circle spawns
            lifetime_frames: How many frames the circle lasts (default: calculated from config)
        """
        cfg = config.get('general', 'items', 'green_circle')
        if lifetime_frames is None:
            # Calculate lifetime_frames from lifetime_seconds and fps
            fps = config.get_fps()
            lifetime_frames = round(cfg['lifetime_seconds'] * fps)
        pic = GreenCirclePic()
        movement = None  # Green circle doesn't move
        layer = cfg['layer']
        super().__init__(position, pic, movement, layer)
        
        self.lifetime_frames = lifetime_frames
        self.current_frame = 0
        self.is_alive = True
    
    def update(self, **kwargs):
        """Update the green circle's state."""
        self.current_frame += 1
        
        # Update visual based on progress
        progress = self.current_frame / self.lifetime_frames
        self.pic.set_radius(progress)
        
        # Check if lifetime expired
        if self.current_frame >= self.lifetime_frames:
            self.is_alive = False
    
    def should_be_destroyed(self) -> bool:
        """
        Check if the green circle should be removed.
        
        Returns:
            True if lifetime has expired
        """
        return not self.is_alive
    
    def get_radius(self) -> float:
        """
        Get the current radius for collision detection.
        
        Returns:
            The current radius
        """
        return self.pic.get_radius()
