
from tkinter import Label, Frame


class Scoreboard(Label):
    
    """Represents the score one has already reached. Increases per destroyed obstacle"""
    
    def __init__(self, master: Frame) -> None:
        self.player_score = 0
        super().__init__(master=master,
                         text=f'Current Score: {self.player_score}',
                         font=("Calibri", 24, "bold"))

    def initialize_scoreboard(self) -> None:
        self.reset_player_score()
        self.config(text=f'Current Score: {self.player_score}',
                    font=("Calibri", 24, "bold"))

    def increase_player_score(self, score: int) -> None:
        
        """Increases the playerscore and updates the gui."""
        
        self.player_score += score
        self.update_score_gui()

    def get_player_score(self) -> int:
        
        """Returns the current value of the players score"""
        
        return self.player_score

    def reset_player_score(self) -> None:
        
        """Resets the current playerscore to zero"""
        
        self.player_score = 0
        self.update_score_gui()

    def lost_game(self) -> None:
        
        """Changes the labeltext according to the current final value and informs the user about his lose"""

        self.config(text=f"You lost. Your final score was '{self.get_player_score()}'")

    def update_score_gui(self) -> None:

        """Updates the score gui"""

        self.config(text=f'Current Score: {self.get_player_score()}')
