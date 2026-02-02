"""Main game loop with 60 FPS."""
import pygame
from src.general.items.background import Background
from src.general.items.white_arrow import WhiteArrow
from src.general.items.red_dot import RedDot
from src.general.items.green_circle import GreenCircle
from src.logic.item_spawn.white_arrow_spawn import WhiteArrowSpawn
from src.logic.item_spawn.red_dot_spawn import RedDotSpawn
from src.logic.item_spawn.green_circle_spawn import GreenCircleSpawn
from src.logic.control.pause import PauseControl
from src.logic.control.end import EndControl
from src.logic.control.bomb import BombControl
from src.logic.collision.red_dot_collide_white_arrow import RedDotCollideWhiteArrow
from src.logic.collision.green_circle_collide_red_dot import GreenCircleCollideRedDot
from src.general.scoring.score_tracker import ScoreTracker
from src.config.config_loader import config


class GameLoop:
    """Main game loop that handles game logic at 60 FPS."""
    
    def __init__(self, screen_width: int = None, screen_height: int = None):
        """
        Initialize the game loop.
        
        Args:
            screen_width: Width of the game screen (default: from config)
            screen_height: Height of the game screen (default: from config)
        """
        if screen_width is None:
            screen_width = config.get_screen_width()
        if screen_height is None:
            screen_height = config.get_screen_height()
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.fps = config.get_fps()
        self.clock = pygame.time.Clock()
        
        # Controls
        self.pause_control = PauseControl()
        self.end_control = EndControl()
        self.bomb_control = BombControl(fps=self.fps)
        
        # Spawn logic
        self.white_arrow_spawn = WhiteArrowSpawn(screen_width, screen_height)
        self.red_dot_spawn = RedDotSpawn(screen_width, screen_height)
        self.green_circle_spawn = GreenCircleSpawn()
        
        # Collision detection
        self.red_dot_white_arrow_collision = RedDotCollideWhiteArrow()
        self.green_circle_red_dot_collision = GreenCircleCollideRedDot()
        
        # Scoring
        self.score_tracker = ScoreTracker(self.fps)
        
        # Game objects
        self.background = Background()
        self.white_arrow = None
        self.red_dots = []
        self.green_circles = []
        
        # Spawn timing (calculated from config)
        game_loop_cfg = config.get('general', 'game_loop')
        # Calculate frames_per_spawn from fps and red_dot_spawn_per_second
        self.frames_per_spawn = round(self.fps / game_loop_cfg['red_dot_spawn_per_second'])
        self.frame_counter = 0
        
        # Game state
        self.game_over = False
        self.last_score = 0
    
    def initialize_game(self):
        """Initialize or reset the game state."""
        # Reset controls
        self.pause_control.reset()
        self.end_control.reset()
        self.bomb_control.reset()
        
        # Reset spawn logic
        self.white_arrow_spawn.reset()
        
        # Reset scoring
        self.score_tracker.reset()
        
        # Spawn white arrow
        arrow_position = self.white_arrow_spawn.spawn()
        self.white_arrow = WhiteArrow(arrow_position)
        
        # Clear game objects
        self.red_dots = []
        self.green_circles = []
        
        # Reset frame counter
        self.frame_counter = 0
        
        # Reset game state
        self.game_over = False
    
    def handle_events(self):
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            self.pause_control.handle_event(event)
            self.end_control.handle_event(event)
            self.bomb_control.handle_event(event)
        
        return True
    
    def update(self):
        """Update game state."""
        # Don't update if paused or game over
        if self.pause_control.is_paused() or self.game_over:
            return
        
        # Update score (time survived)
        self.score_tracker.update_time()
        
        # Update bomb cooldown
        self.bomb_control.update()
        
        # Update white arrow position
        if self.white_arrow:
            self.white_arrow.update()
        
        # Update red dots (they chase the white arrow)
        if self.white_arrow:
            for red_dot in self.red_dots:
                red_dot.update(target_position=self.white_arrow.position)
        
        # Update green circles
        for green_circle in self.green_circles[:]:
            green_circle.update()
            if green_circle.should_be_destroyed():
                self.green_circles.remove(green_circle)
        
        # Handle bomb activation
        if self.bomb_control.should_activate_bomb() and self.white_arrow:
            spawn_position = self.green_circle_spawn.spawn(self.white_arrow.position)
            self.green_circles.append(GreenCircle(spawn_position))
        
        # Spawn red dots (5 per second)
        self.frame_counter += 1
        if self.frame_counter >= self.frames_per_spawn:
            self.frame_counter = 0
            # Spawn a new red dot
            if self.white_arrow:
                spawn_position = self.red_dot_spawn.spawn(self.white_arrow.position)
                self.red_dots.append(RedDot(spawn_position))
        
        # Collision detection
        self.handle_collisions()
    
    def handle_collisions(self):
        """Handle all collision detection and responses."""
        # Check red dot vs white arrow (game over)
        if self.red_dot_white_arrow_collision.check_all_collisions(self.red_dots, self.white_arrow):
            self.game_over = True
            self.last_score = self.score_tracker.get_total_score()
            return
        
        # Check green circle vs red dots (destroy red dots)
        red_dots_to_destroy = self.green_circle_red_dot_collision.check_all_collisions(
            self.green_circles, self.red_dots
        )
        
        # Remove destroyed red dots and update score
        for red_dot in red_dots_to_destroy:
            if red_dot in self.red_dots:
                self.red_dots.remove(red_dot)
                self.score_tracker.add_red_dot_destroyed()
    
    def draw(self, screen: pygame.Surface):
        """
        Draw all game objects.
        
        Args:
            screen: The pygame Surface to draw on
        """
        # Collect all items and sort by layer
        items = [self.background]
        if self.white_arrow:
            items.append(self.white_arrow)
        items.extend(self.red_dots)
        items.extend(self.green_circles)
        
        # Sort by layer (background first, then foreground)
        items.sort(key=lambda item: item.layer)
        
        # Draw all items
        for item in items:
            item.draw(screen)
        
        # Draw real-time score at top left
        self.draw_score(screen)
        
        # Draw bomb cooldown at bottom left
        self.draw_bomb_cooldown(screen)
        
        # Draw pause indicator if paused
        if self.pause_control.is_paused():
            menu_cfg = config.get('general', 'menu_page', 'menu')
            font = pygame.font.Font(None, menu_cfg['pause_font_size'])
            text = font.render("PAUSED", True, (255, 255, 0))
            text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            screen.blit(text, text_rect)
        
        # Draw game over message
        if self.game_over:
            menu_cfg = config.get('general', 'menu_page', 'menu')
            font = pygame.font.Font(None, menu_cfg['game_over_font_size'])
            text = font.render("GAME OVER", True, (255, 0, 0))
            text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 50))
            screen.blit(text, text_rect)
            
            score_font = pygame.font.Font(None, menu_cfg['game_over_score_font_size'])
            score_text = score_font.render(f"Final Score: {self.last_score}", True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 20))
            screen.blit(score_text, score_rect)
            
            instruction_font = pygame.font.Font(None, menu_cfg['game_over_instruction_font_size'])
            instruction_text = instruction_font.render("Press ESC to return to menu", True, (200, 200, 200))
            instruction_rect = instruction_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 80))
            screen.blit(instruction_text, instruction_rect)
    
    def draw_score(self, screen: pygame.Surface):
        """
        Draw the real-time score at the top left corner.
        
        Args:
            screen: The pygame Surface to draw on
        """
        score_breakdown = self.score_tracker.get_score_breakdown()
        score_cfg = config.get('general', 'scoring', 'score_tracker')
        
        font = pygame.font.Font(None, score_cfg['score_font_size'])
        y_offset = score_cfg['score_position_y']
        
        # Total score
        total_text = font.render(f"Score: {score_breakdown['total']}", True, tuple(score_cfg['score_color']))
        screen.blit(total_text, (score_cfg['score_position_x'], y_offset))
        y_offset += score_cfg['breakdown_line_spacing']
        
        # Breakdown
        small_font = pygame.font.Font(None, score_cfg['breakdown_font_size'])
        time_text = small_font.render(f"Time: {score_breakdown['seconds']}s", True, tuple(score_cfg['breakdown_color']))
        screen.blit(time_text, (score_cfg['score_position_x'], y_offset))
        y_offset += score_cfg['line_spacing']
        
        dots_text = small_font.render(f"Dots: {score_breakdown['red_dots']}", True, tuple(score_cfg['breakdown_color']))
        screen.blit(dots_text, (score_cfg['score_position_x'], y_offset))
    
    def draw_bomb_cooldown(self, screen: pygame.Surface):
        """
        Draw the bomb cooldown at the bottom left corner.
        
        Args:
            screen: The pygame Surface to draw on
        """
        score_cfg = config.get('general', 'scoring', 'score_tracker')
        font = pygame.font.Font(None, score_cfg['score_font_size'])
        
        cooldown_remaining = self.bomb_control.get_cooldown_seconds_remaining()
        
        if cooldown_remaining > 0:
            # Show cooldown time with 2 decimal precision
            text = font.render(f"Bomb: {cooldown_remaining:.2f}s", True, (255, 100, 100))
        else:
            # Show "READY" when available
            text = font.render("Bomb: READY", True, (100, 255, 100))
        
        # Position at bottom left
        x_position = score_cfg['score_position_x']
        y_position = self.screen_height - score_cfg['score_position_y'] - 40
        screen.blit(text, (x_position, y_position))
    
    def get_last_score(self) -> int:
        """
        Get the last game score.
        
        Returns:
            The last score achieved
        """
        return self.last_score
    
    def run(self, screen: pygame.Surface) -> bool:
        """
        Run the game loop.
        
        Args:
            screen: The pygame Surface to draw on
            
        Returns:
            True if should continue to next iteration, False if should return to menu
        """
        # Initialize game on first run
        if self.white_arrow is None:
            self.initialize_game()
        
        # Handle events
        if not self.handle_events():
            return False
        
        # Check if should end and return to menu
        if self.end_control.should_end_game():
            return False
        
        # Update game state
        self.update()
        
        # Draw everything
        self.draw(screen)
        
        # Update display
        pygame.display.flip()
        
        # Maintain 60 FPS
        self.clock.tick(self.fps)
        
        return True
