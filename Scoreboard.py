

class Scoreboard:
    """Represents the score one has already reached. Increases per destroyed obstacle"""
    
    PlayerScore = 0

    def set_score(self, score:int) -> None:
        PlayerScore += score

    def reset_score(self) -> None:
        PlayerScore = 0

    