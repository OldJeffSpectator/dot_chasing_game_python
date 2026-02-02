"""White arrow game item."""
from src.general.position import Position
from src.media.pics.white_arrow_pic import WhiteArrowPic
from src.logic.movement.mouse_chase import MouseChase
from src.config.config_loader import config
from .base_item import BaseItem


class WhiteArrow(BaseItem):
    """A white arrow that follows the mouse cursor."""
    
    def __init__(self, position: Position, speed: float = None):
        """
        Initialize a white arrow.
        
        Args:
            position: The initial position of the white arrow
            speed: The movement speed (default: from config)
        """
        cfg = config.get('general', 'items', 'white_arrow')
        if speed is None:
            speed = cfg['default_speed']
        pic = WhiteArrowPic()
        movement = MouseChase(speed=speed)
        layer = cfg['layer']
        super().__init__(position, pic, movement, layer)
    
    def update(self, **kwargs):
        """Update the white arrow's state and rotation."""
        super().update(**kwargs)
        # Update rotation based on movement direction
        if self.movement:
            dx, dy = self.movement.get_last_direction()
            self.pic.set_rotation_from_direction(dx, dy)