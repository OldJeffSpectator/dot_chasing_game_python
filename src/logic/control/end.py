"""End/exit control for the game."""
import pygame


class EndControl:
    """Handles ending the game and returning to menu."""
    
    def __init__(self):
        """Initialize the end control."""
        self.should_end = False
    
    def handle_event(self, event: pygame.event.Event):
        """
        Handle keyboard events for end control.
        
        Args:
            event: The pygame event to handle
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.should_end = True
    
    def should_end_game(self) -> bool:
        """
        Check if the game should end and return to menu.
        
        Returns:
            True if should end, False otherwise
        """
        return self.should_end
    
    def reset(self):
        """Reset the end state."""
        self.should_end = False
