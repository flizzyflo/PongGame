
from GameBoard import GameBoard
from tkinter import *
from Ball import Ball
from Plank import Plank

def main():
    root = Tk()
    root.title("Playstation 5 Spiel")
    gameboard = GameBoard(root, 400,300,"black")

    planke = Plank(gameboard)
    planke.create_plank()

    item = Ball(gameboard, planke, 2)
    item.create_ball()

    gameboard.canvasItem.focus_set()

    gameboard.canvasItem.bind("<a>", lambda event: planke.move_left())
    gameboard.canvasItem.bind("<s>", lambda event: item.random_start())
    gameboard.canvasItem.bind("<d>", lambda event: planke.move_right())


    gameboard.main()

if __name__ == "__main__":
    main()
