"""Red dot game item."""
from src.general.position import Position
from src.media.pics.red_dot_pic import RedDotPic
from src.logic.movement.target_chase import TargetChase
from src.config.config_loader import config
from .base_item import BaseItem


class RedDot(BaseItem):
    """A red dot that chases the white arrow."""
    
    def __init__(self, position: Position, speed: float = None):
        """
        Initialize a red dot.
        
        Args:
            position: The initial position of the red dot
            speed: The movement speed (default: from config)
        """
        cfg = config.get('general', 'items', 'red_dot')
        if speed is None:
            speed = cfg['default_speed']
        pic = RedDotPic()
        movement = TargetChase(speed=speed)
        layer = cfg['layer']
        super().__init__(position, pic, movement, layer)
