
from Scoreboard import Scoreboard
from tkinter import Canvas

class GameBoard(Canvas):

    def __init__(self, root_window: object, width: int, height: int, bgColour: str) -> None:
        super().__init__(master = root_window, width= width, height= height, bg= bgColour)
        self.WIDTH = width
        self.HEIGHT = height
        self.root = root_window
        self.scoreboard = Scoreboard(self.root)

    def get_width(self) -> int:
        return self.WIDTH

    def get_height(self) -> int:
        return self.HEIGHT

    