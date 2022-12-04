
from tkinter import Label

class Scoreboard(Label):
    
    """Represents the score one has already reached. Increases per destroyed obstacle"""
    
    def __init__(self, master: object) -> None:
        self.player_score = 0
        super().__init__(master= master, 
                         text= f'Current Score: {self.player_score}', 
                         font= ("Calibri", 24, "bold"))
        self.master = master

    def initialize_scoreboard(self) -> None:
        self.reset_playerscore()
        self.config(text= f'Current Score: {self.player_score}', 
                    font= ("Calibri", 24, "bold"))

    def increase_playerscore(self, score: int) -> None:
        
        """Increases the playerscore and updates the gui."""
        
        self.player_score += score
        self.update_score_gui()

    def get_playerscore(self) -> int:
        
        """Returns the current value of the players score"""
        
        return self.player_score

    def reset_playerscore(self) -> None:
        
        """Resets the current playerscore to zero"""
        
        self.player_score = 0
        self.update_score_gui()


    def lost_game(self) -> None:
        
        """Changes the labeltext according to the current final value and informs the user about his lose"""

        self.config(text= f"You lost. Your final score was '{self.get_playerscore()}'")


    def update_score_gui(self) -> None:

        """Updates the score gui"""

        self.config(text= f'Current Score: {self.get_playerscore()}')
