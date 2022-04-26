

from Scoreboard import Scoreboard
from tkinter import *

class GameBoard:

    def __init__(self, root_window: object, width: int, height: int, bgColour: str) -> None:
        self.WIDTH = width
        self.HEIGHT = height
        self.root = root_window
        self.BACKGROUDCOLOUR = bgColour
        self.canvasItem = Canvas(self.root, width= self.WIDTH, height= self.HEIGHT, bg= self.BACKGROUDCOLOUR)
        self.canvasItem.pack()
        self.scoreboard = Scoreboard(self.root)

    def get_width(self) -> int:
        return self.WIDTH


    def get_height(self) -> int:
        return self.HEIGHT


    def main(self) -> None:
        
        self.root.mainloop()

