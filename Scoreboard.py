

class Scoreboard:
    """Represents the score one has already reached. Increases per destroyed obstacle"""
    
    def __init__(self) -> None:
        self.PlayerScore = 0

    def increase_playerscore(self, score:int) -> None:
        self.PlayerScore += score

    def reset_playerscore(self) -> None:
        self.PlayerScore = 0

    