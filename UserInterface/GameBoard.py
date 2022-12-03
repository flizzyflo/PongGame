
from tkinter import Canvas
from GameObjects.Ball import Ball
from GameObjects.GameItem import GameItem
from GameObjects.Plank import Plank
from Settings.Settings import PLANK_SPEED, BALL_SPEED, BALL_SIZE, SCORE_VALUE
from UserInterface.Scoreboard import Scoreboard

class GameBoard(Canvas):

    def __init__(self, master: object, gameboard_width: int, gameboard_height: int, gameboard_background_colour: str, scoreboard_object: Scoreboard) -> None:
        super().__init__(master = master, width= gameboard_width, height= gameboard_height, bg= gameboard_background_colour)
        self.gameboard_width = gameboard_width
        self.gameboard_height = gameboard_height

        self.plank = Plank(self, PLANK_SPEED)
        self.plank.create_plank(self.gameboard_width // 2 - 20, self.gameboard_height - 20)

        self.ball = Ball(self, self.plank.plank, BALL_SPEED, BALL_SIZE)
        self.ball.create_ball()

        self.scoreboard = scoreboard_object
        
    def get_coords(self, game_object: GameItem) -> tuple[int]:
        return self.bbox(game_object)

    def get_width(self) -> int:
        return self.gameboard_width

    def get_height(self) -> int:
        return self.gameboard_height

    def increase_playerscore(self) -> None:
        self.scoreboard.increase_playerscore(SCORE_VALUE)
