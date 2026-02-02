"""Score tracking system."""


class ScoreTracker:
    """Tracks the player's score based on time survived and red dots destroyed."""
    
    def __init__(self, fps: int = 60):
        """
        Initialize the score tracker.
        
        Args:
            fps: Frames per second for time calculation
        """
        self.fps = fps
        self.frames_survived = 0
        self.red_dots_destroyed = 0
    
    def update_time(self):
        """Increment the frame counter (call every frame)."""
        self.frames_survived += 1
    
    def add_red_dot_destroyed(self, count: int = 1):
        """
        Add destroyed red dots to the score.
        
        Args:
            count: Number of red dots destroyed
        """
        self.red_dots_destroyed += count
    
    def get_seconds_survived(self) -> float:
        """
        Get the number of seconds survived.
        
        Returns:
            Seconds survived
        """
        return self.frames_survived / self.fps
    
    def get_total_score(self) -> int:
        """
        Calculate the total score.
        Score = seconds survived + red dots destroyed
        
        Returns:
            The total score
        """
        return int(self.get_seconds_survived()) + self.red_dots_destroyed
    
    def get_score_breakdown(self) -> dict:
        """
        Get a breakdown of the score components.
        
        Returns:
            Dictionary with score breakdown
        """
        return {
            'seconds': int(self.get_seconds_survived()),
            'red_dots': self.red_dots_destroyed,
            'total': self.get_total_score()
        }
    
    def reset(self):
        """Reset the score tracker."""
        self.frames_survived = 0
        self.red_dots_destroyed = 0
