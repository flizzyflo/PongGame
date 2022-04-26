

class Scoreboard:
    """Represents the score one has already reached. Increases per destroyed obstacle"""
    
    def __init__(self) -> None:
        self.player_score = 0

    def increase_playerscore(self, score:int) -> None:
        self.player_score += score

    def get_playerscore(self) -> int:
        return self.player_score

    def reset_playerscore(self) -> None:
        self.player_score = 0

    