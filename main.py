from Settings.Settings import FRAME_BORDERWIDTH
from tkinter import Button, Label, Frame, BOTH, GROOVE
from UserInterface.GameBoard import GameBoard
from UserInterface.Scoreboard import Scoreboard

from UserInterface.main_window import MainWindow

def main() -> None:
    root = MainWindow()

    information_frame = Frame(root, relief= GROOVE, borderwidth= FRAME_BORDERWIDTH)
    information_frame.pack(fill=BOTH)

    gameboard_frame = Frame(root, relief=GROOVE, borderwidth= FRAME_BORDERWIDTH)
    gameboard_frame.pack()

    scoreboard = Scoreboard(master= information_frame)
    scoreboard.pack()
    Label(information_frame, text= "Press 'A' to move left\nPress 'D' to move right").pack()
    start_button = Button(master= information_frame, text= "Start game")
    start_button.pack(fill= BOTH)

    gameboard = GameBoard(master= gameboard_frame, gameboard_width= 400, gameboard_height= 300, gameboard_background_colour= "black", scoreboard_object= scoreboard)
    gameboard.pack()
    gameboard.focus_set()
    gameboard.bind("<a>", lambda event: gameboard.plank.move_left())
    gameboard.bind("<d>", lambda event: gameboard.plank.move_right())

    start_button.config(command= lambda: gameboard.ball.random_start())

    root.mainloop()
    

if __name__ == '__main__':
    main()
