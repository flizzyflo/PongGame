from GameItem import GameItem
from tkinter import *
from random import randrange


class Ball(GameItem):

    def __init__(self, GameBoardObject: object, PlankObject: list[object], speed: int, size: int = 15, colour: str = "blue") -> None:
        super().__init__(GameBoardObject, speed)
        self.size = size
        self.colour = colour
        self.plank_object = PlankObject
        self.x = 0
        self.y = 0
        self.game_over = False

        
    def create_ball(self) -> None:
        """Initialization of the ball item"""
        self.ball = self.gameboard.canvasItem.create_oval(self.size, self.size * 3, self.size * 3, self.size * 5, fill=self.colour)


    def random_start(self) -> None:
        """Random selection of a starting direction of the ball"""

        random_value = randrange(0, 3)
        if random_value == 0:
            self.move_left()
            self.move_down()

        elif random_value == 1:
            self.move_right()
            self.move_down()

        elif random_value == 2:
            self.move_left()
            self.move_up()

        elif random_value == 3:
            self.move_right()
            self.move_up()


    def handle_ball_plank_collision(self) -> bool:
        """Checks if the ball hits the plank"""

        plank_left_edge = self.get_coords(self.plank_object.plank)[0]
        plank_right_edge = self.get_coords(self.plank_object.plank)[2]
        plank_upper_edge = self.get_coords(self.plank_object.plank)[1]
        ball_lower_edge = self.get_coords(self.ball)[3]
        ball_lower_x_value = (self.get_coords(self.ball)[0] + self.get_coords(self.ball)[2]) / 2

        if (plank_left_edge <=  ball_lower_x_value <= plank_right_edge) and (plank_upper_edge == ball_lower_edge):
            self.gameboard.scoreboard.increase_playerscore(1)
            self.gameboard.scoreboard.set_score()
            return True

        else:
            return False


    def handle_gameborder_collision(self)-> bool:
        """Function to handle collision of the ball"""
        
        #left border
        if self.get_coords(self.ball)[0] <= 1:
            return True
        
        #right border
        elif self.get_coords(self.ball)[2] >= self.gameboard.get_width() - 1:
            return True

        #upper border
        elif self.get_coords(self.ball)[1] <= 1:
            return True

        #lower border
        elif self.get_coords(self.plank_object.plank)[1] < self.get_coords(self.ball)[3] - 15:
            self.game_over = True


    def move_left(self) -> None:
        """Move the ball left until it hits the left border. Bounces back 
        from the left border of the gameboard rightwards."""

        self.x = - 1

        self.gameboard.canvasItem.move(self.ball, self.x, 0)
     
        if self.handle_gameborder_collision():
            self.move_right()

        else:
            self.gameboard.canvasItem.after(self.speed, self.move_left)


    def move_right(self) -> None:
        """Move the ball right until it hits the right border. Bounces back 
        from the right border of the gameboard leftwards."""

        self.x = 1
        self.gameboard.canvasItem.move(self.ball, self.x, 0)

        if self.handle_gameborder_collision():
            self.move_left()
        
        else:
            self.gameboard.canvasItem.after(self.speed, self.move_right)


    def move_up(self) -> None:
        """Move the ball up until it hits the topmost border. Bounces back 
        from the border of the gameboard downwards."""

        self.y = -1
        self.gameboard.canvasItem.move(self.ball, 0, self.y)

        if self.handle_gameborder_collision():
            self.move_down()

        else:
            self.gameboard.canvasItem.after(self.speed, self.move_up)


    def move_down(self) -> None:
        """Move the ball down until it hits either the plank and bounces back
        or it hits the border. If it hits the lower boundary, the game is over."""

        self.y = 1
        self.gameboard.canvasItem.move(self.ball, 0, self.y)

        if self.handle_ball_plank_collision():
            self.move_up()

        elif self.game_over:
          
            self.x, self.y = 0, 0
            self.gameboard.canvasItem.move(self.ball, 0, 0)
            self.gameboard.canvasItem.destroy()
            self.gameboard.scoreboard.lost_game()

        else:
            self.gameboard.canvasItem.after(self.speed, self.move_down)
        
