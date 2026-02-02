"""Bomb control for spawning green circles."""
import pygame
from src.config.config_loader import config


class BombControl:
    """Handles bomb activation with SPACE key and cooldown."""
    
    def __init__(self, fps: int = None):
        """
        Initialize the bomb control.
        
        Args:
            fps: Frames per second for cooldown calculation (default: from config)
        """
        if fps is None:
            fps = config.get_fps()
        
        cfg = config.get('logic', 'control', 'bomb')
        self.cooldown_seconds = cfg['cooldown_seconds']
        self.cooldown_frames = round(self.cooldown_seconds * fps)
        self.fps = fps
        
        self.bomb_activated = False
        self.space_key_pressed = False
        self.cooldown_remaining = 0  # Frames remaining until next bomb available
    
    def update(self):
        """Update cooldown state (call every frame)."""
        if self.cooldown_remaining > 0:
            self.cooldown_remaining -= 1
    
    def handle_event(self, event: pygame.event.Event):
        """
        Handle keyboard events for bomb control.
        
        Args:
            event: The pygame event to handle
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not self.space_key_pressed:
                # Only activate if cooldown is finished
                if self.cooldown_remaining <= 0:
                    self.bomb_activated = True
                    self.cooldown_remaining = self.cooldown_frames
                self.space_key_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.space_key_pressed = False
    
    def should_activate_bomb(self) -> bool:
        """
        Check if bomb should be activated.
        
        Returns:
            True if SPACE was pressed and cooldown finished, False otherwise
        """
        if self.bomb_activated:
            self.bomb_activated = False  # Reset after checking
            return True
        return False
    
    def get_cooldown_seconds_remaining(self) -> float:
        """
        Get the cooldown time remaining in seconds.
        
        Returns:
            Seconds remaining (0 if ready)
        """
        return max(0, self.cooldown_remaining / self.fps)
    
    def is_ready(self) -> bool:
        """
        Check if bomb is ready to use.
        
        Returns:
            True if cooldown finished, False otherwise
        """
        return self.cooldown_remaining <= 0
    
    def reset(self):
        """Reset the bomb state."""
        self.bomb_activated = False
        self.space_key_pressed = False
        self.cooldown_remaining = 0