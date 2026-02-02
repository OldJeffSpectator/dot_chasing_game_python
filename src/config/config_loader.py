"""Configuration loader for the game."""
import json
import os


class Config:
    """Singleton configuration loader."""
    
    _instance = None
    _config = None
    
    def __new__(cls):
        """Ensure only one instance of Config exists."""
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance
    
    def _load_config(self):
        """Load configuration from config.json."""
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        with open(config_path, 'r') as f:
            self._config = json.load(f)
    
    def get(self, *keys):
        """
        Get a configuration value using a path of keys.
        
        Args:
            *keys: Path to the configuration value
            
        Returns:
            The configuration value
            
        Example:
            config.get('screen', 'width')  # Returns 1600
            config.get('media', 'pics', 'red_dot_pic', 'diameter')  # Returns 15
        """
        value = self._config
        for key in keys:
            value = value[key]
        return value
    
    def get_screen_width(self):
        """Get screen width."""
        return self.get('screen', 'width')
    
    def get_screen_height(self):
        """Get screen height."""
        return self.get('screen', 'height')
    
    def get_fps(self):
        """Get game FPS."""
        return self.get('game', 'fps')
    
    def reload(self):
        """Reload configuration from file."""
        self._load_config()


# Global config instance
config = Config()
