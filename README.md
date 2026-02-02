# Dot Chasing Game

A Python replica of the Tilt to Live game on iPhone 4, recreated from memory.

Control a white arrow with your mouse while avoiding red dots that chase you! Survive as long as possible and destroy enemies with strategic bomb placement.

## Features

- **Mouse-controlled gameplay**: Control the white arrow with your mouse cursor
- **Dynamic rotation**: The arrow automatically rotates to face the direction it's moving
- **Dynamic enemies**: Red dots spawn continuously and chase the white arrow
- **Bomb mechanic**: Press `SPACE` to unleash a green circular wave that destroys red dots (3-second cooldown)
- **Scoring system**: Earn points for time survived (seconds) + red dots destroyed
- **Collision detection**: Game ends when a red dot catches the white arrow
- **Real-time score display**: View your score, time, and dots destroyed in the top-left corner
- **Bomb cooldown display**: View remaining cooldown time (or "READY") at the bottom-left corner
- **Previous score tracking**: See your last game's score on the menu page
- **60 FPS gameplay**: Enjoy smooth animations and responsive controls
- **Pause functionality**: Press `P` to pause/unpause the game at any time
- **Easy navigation**: Press `ESC` to return to the main menu

## Installation

1. Ensure you have Python 3.7+ installed
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## How to Play

Run the game:

```bash
python -m src.main
```

Or:

```bash
python src/main.py
```

### Controls

- **Mouse**: Move the white arrow (arrow faces movement direction)
- **SPACE**: Activate bomb (spawns green wave that destroys red dots)
- **P**: Pause/unpause the game
- **ESC**: Return to main menu
- **Click START GAME**: Begin playing

### Gameplay

- Control the white arrow by moving your mouse
- The arrow automatically rotates to face the direction you're moving
- Avoid the red dots that continuously spawn and chase you
- Red dots spawn at random locations (excluding areas within 50 pixels of your position)
- Five new red dots spawn every second
- Press SPACE to activate a bomb, spawning a green circular wave from your position
- The green wave expands for 0.3 seconds and destroys any red dots it touches
- Bombs have a 3-second cooldown—check the bottom-left corner for the remaining time
- **Game Over**: The game ends when a red dot catches you
- **Scoring**: Earn points for time survived (in seconds) plus red dots destroyed
- Your score is displayed in real-time at the top-left corner
- After game over, your final score is displayed on the menu page
- Try to survive as long as possible and destroy as many red dots as you can!

## Project Structure

```
src/
├── config/
│   ├── config.json          # Centralized configuration for all game parameters
│   └── config_loader.py     # Configuration loader singleton
├── general/
│   ├── position.py          # Position class for object locations
│   ├── items/               # Game objects (red_dot, white_arrow, background, green_circle)
│   ├── menu_page/           # Main menu interface with previous score display
│   ├── scoring/             # Score tracking system
│   └── game_loop.py         # Main game loop at 60 FPS with collision detection
├── logic/
│   ├── movement/            # Movement behaviors (target_chase, mouse_chase)
│   ├── item_spawn/          # Spawn logic for game objects (including green circles)
│   ├── control/             # Game controls (pause, end, bomb)
│   └── collision/           # Collision detection (red_dot vs white_arrow, green_circle vs red_dot)
├── media/
│   └── pics/                # Visual representations of game objects (with rotation support)
└── main.py                  # Game entry point
```

## Architecture

The game follows an object-oriented design with:

- **Abstract Base Classes (ABC)**: Used for pics, movements, and items
- **Layer system**: Objects are rendered in layers (0=background, 1=game objects, 2=effects)
- **Component-based design**: Items combine position, appearance, and movement behavior
- **60 FPS fixed timestep**: Ensures consistent gameplay across different systems
- **Centralized configuration**: All magic numbers stored in `config.json` for easy tuning
- **Config structure**: JSON follows file paths and attribute names for organization

## Configuration

The game uses a centralized configuration system located in `src/config/config.json`. All magic numbers are organized by file path and attribute name:

```json
{
  "screen": { "width": 1600, "height": 1000 },
  "game": { "fps": 60 },
  "media": {
    "pics": {
      "red_dot_pic": { "diameter": 15, "color": [255, 0, 0], ... },
      "white_arrow_pic": { "width": 15, "height": 13, ... },
      ...
    }
  },
  "logic": { "movement": { ... }, "collision": { ... } },
  "general": { "items": { ... }, "game_loop": { ... } }
}
```

You can easily modify game parameters by editing `config.json`, including:
- Movement speeds for arrows and dots
- Colors for all visual elements
- Spawn rates and distances
- Font sizes and positions
- Collision radii
- Bomb cooldown duration
- And much more!

## Game Specifications

- **Screen size**: 1600 × 1000 pixels (width × height)
- **Frame rate**: 60 FPS
- **White arrow**: 15×13 pixels, moves at 10 pixels/frame, rotates to face movement direction
- **Red dots**: 15-pixel diameter (7.5px radius), move at 5 pixels/frame
- **Green wave**: Expands from 30px to 100px radius over 0.3 seconds (18 frames)
- **Spawn rate**: 5 red dots per second
- **Spawn constraint**: Red dots don't spawn within 50 pixels of the white arrow
- **Collision detection**: Red dot radius (7.5px) vs. white arrow position
- **Score formula**: Time survived (seconds) + red dots destroyed
- **Bomb cooldown**: 3 seconds between uses
- **Rendering layers**: Background (0), game objects (1), green waves (2)

## License

See LICENSE file for details.
