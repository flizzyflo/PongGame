
from GameBoard import GameBoard
from tkinter import *
from GameObjects.Ball import Ball
from GameObjects.Plank import Plank
from Settings.Settings import BALL_SPEED, COLOURS, PLANK_SPEED

def main() -> None:
    root = Tk()
    root.title("Playstation 5 Spiel")
    gameboard = GameBoard(root_window= root, width= 400, height= 300, bgColour= "black")
    gameboard.pack()
    plankePlayer1 = Plank(GameBoardObject= gameboard, speed= PLANK_SPEED, colour= COLOURS)
    plankePlayer1.create_plank()

    plankList = [plankePlayer1]

    item = Ball(GameBoardObject = gameboard, PlankObject = plankList, speed = BALL_SPEED)
    item.create_ball()

    gameboard.focus_set()
    gameboard.bind("<a>", lambda event: plankList[0].move_left())
    gameboard.bind("<s>", lambda event: item.random_start())
    gameboard.bind("<d>", lambda event: plankList[0].move_right())

    root.mainloop()
    

if __name__ == '__main__':
    main()
