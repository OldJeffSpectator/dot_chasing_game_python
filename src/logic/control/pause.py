"""Pause control for the game."""
import pygame


class PauseControl:
    """Handles pausing and unpausing the game."""
    
    def __init__(self):
        """Initialize the pause control."""
        self.paused = False
        self.pause_key_pressed = False
    
    def handle_event(self, event: pygame.event.Event):
        """
        Handle keyboard events for pause control.
        
        Args:
            event: The pygame event to handle
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and not self.pause_key_pressed:
                self.paused = not self.paused
                self.pause_key_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_p:
                self.pause_key_pressed = False
    
    def is_paused(self) -> bool:
        """
        Check if the game is currently paused.
        
        Returns:
            True if paused, False otherwise
        """
        return self.paused
    
    def reset(self):
        """Reset the pause state."""
        self.paused = False
        self.pause_key_pressed = False
