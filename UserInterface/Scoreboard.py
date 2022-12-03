
from tkinter import Label

class Scoreboard:
    """Represents the score one has already reached. Increases per destroyed obstacle"""
    
    def __init__(self, RootObject: object) -> None:
        self.player_score = 0
        self.root_object = RootObject
        self.label = Label(master= self.root_object, text=f'Your Score: -> {self.player_score} <-', font=("Calibri", 24, "bold"))
        self.label.pack()

    def increase_playerscore(self, score:int) -> None:
        self.player_score += score

    def get_playerscore(self) -> int:
        return self.player_score

    def reset_playerscore(self) -> None:
        self.player_score = 0

    def lost_game(self) -> None:
        self.label.destroy()
        Label(master= self.root_object, text= f'Sorry, you lost!', font=("Calibri", 32, "bold")).pack()
        Label(master= self.root_object, text= f'Your Score: -> {self.player_score} <-', font=("Calibri", 48, "bold")).pack()

    def set_score(self) -> None:
        self.label.config(text= f'Your Score: -> {self.player_score} <-')