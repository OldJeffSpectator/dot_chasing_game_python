"""Main menu page with START_GAME button."""
import pygame
from src.config.config_loader import config


class MenuPage:
    """Main menu page for the game."""
    
    def __init__(self, screen_width: int = None, screen_height: int = None):
        """
        Initialize the menu page.
        
        Args:
            screen_width: Width of the screen (default: from config)
            screen_height: Height of the screen (default: from config)
        """
        if screen_width is None:
            screen_width = config.get_screen_width()
        if screen_height is None:
            screen_height = config.get_screen_height()
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Load config
        cfg = config.get('general', 'menu_page', 'menu')
        
        # Button properties
        self.button_width = cfg['button_width']
        self.button_height = cfg['button_height']
        self.button_x = (screen_width - self.button_width) // 2
        self.button_y = (screen_height - self.button_height) // 2
        self.button_rect = pygame.Rect(
            self.button_x, self.button_y, 
            self.button_width, self.button_height
        )
        
        # Colors
        self.bg_color = tuple(cfg['bg_color'])
        self.button_color = tuple(cfg['button_color'])
        self.button_hover_color = tuple(cfg['button_hover_color'])
        self.text_color = tuple(cfg['text_color'])
        self.score_color = tuple(cfg['score_color'])
        self.instruction_color = tuple(cfg['instruction_color'])
        
        # Fonts
        self.title_font = pygame.font.Font(None, cfg['title_font_size'])
        self.button_font = pygame.font.Font(None, cfg['button_font_size'])
        self.score_font = pygame.font.Font(None, cfg['score_font_size'])
        self.instruction_font = pygame.font.Font(None, cfg['instruction_font_size'])
        
        # State
        self.start_game = False
        self.previous_score = None
    
    def handle_events(self):
        """Handle menu events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if self.button_rect.collidepoint(event.pos):
                        self.start_game = True
        
        return True
    
    def set_previous_score(self, score: int):
        """
        Set the previous game score to display.
        
        Args:
            score: The score from the last game
        """
        if score > 0:
            self.previous_score = score
    
    def draw(self, screen: pygame.Surface):
        """
        Draw the menu page.
        
        Args:
            screen: The pygame Surface to draw on
        """
        # Draw background
        screen.fill(self.bg_color)
        
        # Draw title
        title_text = self.title_font.render("Dot Chasing Game", True, self.text_color)
        title_rect = title_text.get_rect(center=(self.screen_width // 2, self.screen_height // 4))
        screen.blit(title_text, title_rect)
        
        # Draw previous score if available
        if self.previous_score is not None:
            score_text = self.score_font.render(f"Your previous game score is {self.previous_score}", True, self.score_color)
            score_rect = score_text.get_rect(center=(self.screen_width // 2, self.screen_height // 3 + 20))
            screen.blit(score_text, score_rect)
        
        # Check if mouse is hovering over button
        mouse_pos = pygame.mouse.get_pos()
        is_hovering = self.button_rect.collidepoint(mouse_pos)
        
        # Draw button
        button_color = self.button_hover_color if is_hovering else self.button_color
        pygame.draw.rect(screen, button_color, self.button_rect, border_radius=10)
        pygame.draw.rect(screen, self.text_color, self.button_rect, width=3, border_radius=10)
        
        # Draw button text
        button_text = self.button_font.render("START GAME", True, self.text_color)
        button_text_rect = button_text.get_rect(center=self.button_rect.center)
        screen.blit(button_text, button_text_rect)
        
        # Draw instructions
        instructions = [
            "Control the white arrow with your mouse",
            "Avoid the red dots!",
            "",
            "Press SPACE to activate bomb",
            "Press P to pause",
            "Press ESC to return to menu"
        ]
        
        y_offset = self.screen_height * 2 // 3
        for instruction in instructions:
            text = self.instruction_font.render(instruction, True, self.instruction_color)
            text_rect = text.get_rect(center=(self.screen_width // 2, y_offset))
            screen.blit(text, text_rect)
            y_offset += 40
        
        pygame.display.flip()
    
    def should_start_game(self) -> bool:
        """
        Check if the game should start.
        
        Returns:
            True if START_GAME button was clicked
        """
        return self.start_game
    
    def reset(self):
        """Reset the menu state."""
        self.start_game = False
        # Don't reset previous_score - it persists across menu views
    
    def run(self, screen: pygame.Surface) -> bool:
        """
        Run the menu page.
        
        Args:
            screen: The pygame Surface to draw on
            
        Returns:
            True if should start game, False if should quit
        """
        self.reset()
        clock = pygame.time.Clock()
        
        while True:
            if not self.handle_events():
                return False
            
            if self.should_start_game():
                return True
            
            self.draw(screen)
            clock.tick(60)
