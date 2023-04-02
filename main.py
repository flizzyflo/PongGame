from game_objects.static_objects.obstacle import Obstacle
from settings.settings import FRAME_BORDERWIDTH, GAMEBOARD_HEIGTH, GAMEBOARD_WIDTH, TITLE
from tkinter import Button, Label, Frame, BOTH, GROOVE
from userinterface.gameboard import GameBoard
from userinterface.scoreboard import Scoreboard

from userinterface.main_window import MainWindow


def main() -> None:
    root = MainWindow()
    root.title(TITLE)

    information_frame = Frame(master=root,
                              relief=GROOVE,
                              borderwidth=FRAME_BORDERWIDTH)
    information_frame.pack(fill=BOTH)

    gameboard_frame = Frame(master=root,
                            relief=GROOVE, 
                            borderwidth=FRAME_BORDERWIDTH)
    gameboard_frame.pack()

    scoreboard = Scoreboard(master=information_frame)
    scoreboard.pack()
    Label(master=information_frame,
          text="Press 'A' to move left\nPress 'D' to move right").pack()
    
    start_game_button = Button(master=information_frame,
                               text="Start game")
    start_game_button.pack(fill=BOTH)

    gameboard = GameBoard(master=gameboard_frame,
                          gameboard_width=GAMEBOARD_WIDTH,
                          gameboard_height=GAMEBOARD_HEIGTH,
                          gameboard_background_colour="black",
                          scoreboard_object=scoreboard,
                          start_button=start_game_button)
    gameboard.pack()
    gameboard.focus_set()
    gameboard.bind("<a>", lambda event: gameboard.plank.move_left())
    gameboard.bind("<d>", lambda event: gameboard.plank.move_right())

    start_game_button.config(command=lambda: gameboard.ball.random_start())

    root.mainloop()
    

if __name__ == '__main__':
    
    main()
