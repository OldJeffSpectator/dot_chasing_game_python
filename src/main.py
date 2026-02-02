"""Main entry point for the Dot Chasing Game."""
import pygame
from src.general.menu_page.menu import MenuPage
from src.general.game_loop import GameLoop
from src.config.config_loader import config


def main():
    """Main function to start the game."""
    # Initialize pygame
    pygame.init()
    
    # Screen dimensions from config
    screen_width = config.get_screen_width()
    screen_height = config.get_screen_height()
    
    # Create screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Dot Chasing Game")
    
    # Create menu and game loop
    menu = MenuPage(screen_width, screen_height)
    game_loop = GameLoop(screen_width, screen_height)
    
    # Main game state loop
    running = True
    in_game = False
    
    while running:
        if not in_game:
            # Show menu and wait for start
            should_start = menu.run(screen)
            if not should_start:
                running = False
            else:
                in_game = True
                game_loop.initialize_game()
        else:
            # Run game loop
            continue_game = game_loop.run(screen)
            if not continue_game:
                # Return to menu and display last score
                last_score = game_loop.get_last_score()
                menu.set_previous_score(last_score)
                in_game = False
    
    # Quit pygame
    pygame.quit()


if __name__ == "__main__":
    main()
