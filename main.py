
from GameBoard import GameBoard
from tkinter import *
from Ball import Ball
from Plank import Plank

def main() -> None:
    root = Tk()
    root.title("Playstation 5 Spiel")
    gameboard = GameBoard(root_window= root, width= 400, height= 300, bgColour= "black")
  
    plankePlayer1 = Plank(GameBoardObject= gameboard)
    plankePlayer1.create_plank()

    plankePlayer2 = Plank(GameBoardObject= gameboard, colour="blue")
    plankePlayer2.create_plank()

    plankList = [plankePlayer1, plankePlayer2]

    item = Ball(GameBoardObject = gameboard, PlankObject = plankList, speed = 5)
    item.create_ball()

    gameboard.canvasItem.focus_set()
    gameboard.canvasItem.bind("<a>", lambda event: plankList[0].move_left())
    gameboard.canvasItem.bind("<s>", lambda event: item.random_start())
    gameboard.canvasItem.bind("<d>", lambda event: plankList[0].move_right())

    gameboard.main()


if __name__ == '__main__':
    main()
