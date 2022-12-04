
from tkinter import Canvas, Button, DISABLED, NORMAL
from GameObjects.Ball import Ball
from GameObjects.GameItem import GameItem
from GameObjects.Plank import Plank
from Settings.Settings import PLANK_SPEED, BALL_SPEED, BALL_SIZE, SCORE_VALUE, MODULO_FOR_DIFFICULTY, PLANK_SIZE_REDUCTION
from UserInterface.Scoreboard import Scoreboard

class GameBoard(Canvas):

    def __init__(self, master: object, gameboard_width: int, gameboard_height: int, gameboard_background_colour: str, scoreboard_object: Scoreboard, start_button: Button) -> None:
        super().__init__(master = master, 
                         width= gameboard_width, 
                         height= gameboard_height, 
                         bg= gameboard_background_colour)
                         
        self.gameboard_width = gameboard_width
        self.gameboard_height = gameboard_height
        self.initialize_gameboard()
        self.scoreboard = scoreboard_object
        self.lost_game = False
        self.start_button = start_button


    def game_started(self) -> None:
        self.start_button.config(state=DISABLED)


    def set_game_status(self, lost: bool) -> None:
        self.lost_game = lost
        if self.game_is_lost():
            self.start_button.config(text= "Restart Game", 
                                     command= lambda: self.restart_game(), 
                                     state= NORMAL)


    def game_is_lost(self) -> bool:

        """Returns the current game status"""

        return self.lost_game


    def initialize_gameboard(self) -> None:

        """Initializes the plank and ball item"""

        self.plank = Plank(self, PLANK_SPEED)
        self.plank.create_plank(self.gameboard_width // 2 - 20, self.gameboard_height - 20)
        self.ball = Ball(self, self.plank.plank, BALL_SPEED, BALL_SIZE)
        self.ball.create_ball()

        self.initial_ball_coords = self.coords(self.ball)


    def restart_game(self) -> None:
        
        """Restarts the game. Deletes the existing widgets and creates new."""

        self.delete("plank")
        self.delete("ball")
        self.scoreboard.initialize_scoreboard()
        self.initialize_gameboard()
        self.start_button.config(text= "Start game", 
                                 command= lambda: self.ball.random_start(), 
                                 state= NORMAL)
        self.set_game_status(False)


    def get_gameboard_widget_coords(self, game_object: GameItem) -> tuple[int]:
        
        """Returns the coordinats of an widget of this gameboard item as a tuple.
        Tuple has value order x1, y1, x2, y2"""

        return self.coords(game_object)


    def get_width(self) -> int:

        """Returns the width of the gameboard"""

        return self.gameboard_width


    def get_height(self) -> int:

        """Returns the height of the gameboard"""

        return self.gameboard_height


    def manage_score_and_difficulty(self) -> None:
        
        """Manages displaying the current score as well as taking care of the difficulty, which depends on the current score"""
        
        self.increase_playerscore()
        if self.need_to_reduce():
            self.increase_difficulty()


    def increase_playerscore(self) -> None:
        
        """Increases the playerscore"""
        
        self.scoreboard.increase_playerscore(SCORE_VALUE)
    

    def need_to_reduce(self) -> bool:
        
        """Checks whether the difficulty needs to be increased. Every 10 score points, it returns true"""

        return self.scoreboard.get_playerscore() % MODULO_FOR_DIFFICULTY == 0


    def increase_difficulty(self) -> None:
        
        """Reduces the plank size to increase the difficulty. Stops at a certain point to keep the game playable"""

        x1, y1, x2, y2 = self.coords(self.plank.plank)
        if (x2 - x1 > 20):
            x2 = x2 - PLANK_SIZE_REDUCTION
            self.coords(self.plank.plank, x1, y1, x2, y2)
