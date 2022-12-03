
from tkinter import Label

class Scoreboard(Label):
    """Represents the score one has already reached. Increases per destroyed obstacle"""
    
    def __init__(self, master: object) -> None:
        self.player_score = 0
        super().__init__(master= master, text= f'Current Score: {self.player_score}', font= ("Calibri", 24, "bold"))
        self.master = master

    def increase_playerscore(self, score: int) -> None:
        self.player_score += score
        self.set_score()

    def get_playerscore(self) -> int:
        return self.player_score

    def reset_playerscore(self) -> None:
        self.player_score = 0

    def lost_game(self) -> None:
        self.destroy()
        Label(master= self.master, text= f'Sorry, you lost!', font=("Calibri", 32, "bold")).pack()
        Label(master= self.master, text= f'Your Score: -> {self.player_score} <-', font=("Calibri", 48, "bold")).pack()

    def set_score(self) -> None:
        self.config(text= f'Your Score: -> {self.player_score} <-')