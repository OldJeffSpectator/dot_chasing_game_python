"""Background game item."""
from src.general.position import Position
from src.media.pics.background_pic import BackgroundPic
from src.config.config_loader import config
from .base_item import BaseItem


class Background(BaseItem):
    """The game background."""
    
    def __init__(self):
        """Initialize the background."""
        cfg = config.get('general', 'items', 'background')
        position = Position(0, 0)
        pic = BackgroundPic()
        movement = None  # Background doesn't move
        layer = cfg['layer']
        super().__init__(position, pic, movement, layer)
    
    def update(self, **kwargs):
        """Background doesn't need to update."""
        pass  # Background is static
