
from tkinter import *
from random import randrange

from GameObjects.GameItem import GameItem
from GameObjects.Plank import Plank
from Settings.Settings import COLOURS, BALL_TAG


class Ball(GameItem):

    """Class to represent the ball object. manages the collission of the ball as well as the positioning of the ball."""

    def __init__(self, game_board: object, plank: Plank, ball_speed: int, ball_size: int) -> None:
        
        super().__init__(game_board, ball_speed)
        self.gameboard = game_board
        self.ball_size = ball_size
        self.ball_colour = COLOURS[randrange(0, len(COLOURS) - 1)]

        self.plank = plank
        self.x_velocity = 0
        self.y_velocity = 0


    def create_ball(self) -> None:
        
        """Initialization of the ball item"""
        
        self.ball = self.gameboard.create_oval(self.ball_size + 30, 
                                               self.ball_size * 3 + 30, 
                                               self.ball_size * 3 + 30, 
                                               self.ball_size * 5 + 30, 
                                               fill=self.ball_colour,
                                               tags= BALL_TAG)


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

        self.gameboard.game_started()

    def handle_ball_plank_collision(self) -> bool:
        
        """Checks if the ball hits the plank"""
    
        plank_left_edge = self.gameboard.get_gameboard_widget_coords(self.plank)[0] #x1 value
        plank_upper_edge = self.gameboard.get_gameboard_widget_coords(self.plank)[1] #y1 value
        plank_right_edge = self.gameboard.get_gameboard_widget_coords(self.plank)[2] #x2 value
        ball_lower_edge = self.gameboard.get_gameboard_widget_coords(self.ball)[3] #y2 value

        ball_left_edge = self.gameboard.get_gameboard_widget_coords(self.ball)[0]
        ball_right_edge = self.gameboard.get_gameboard_widget_coords(self.ball)[2]
        ball_center_value = (ball_right_edge + ball_left_edge) //2

        if (plank_left_edge <= ball_center_value <= plank_right_edge) and (plank_upper_edge == ball_lower_edge):
        
            self.gameboard.manage_score_and_difficulty()
            return True

        else:
            return False


    def handle_gameborder_collision(self)-> bool:
        
        """Function to handle collision of the ball"""
        
        # left border
        if self.gameboard.get_gameboard_widget_coords(self.ball)[0] <= 1:
            return True
        
        #right border
        elif self.gameboard.get_gameboard_widget_coords(self.ball)[2] >= self.gameboard.get_width() - 1:
            return True

        #upper border
        elif self.gameboard.get_gameboard_widget_coords(self.ball)[1] <= 1:
            return True

        #lower border
        elif self.gameboard.get_gameboard_widget_coords(self.plank)[1] < self.gameboard.get_gameboard_widget_coords(self.ball)[3] - 15:
            self.gameboard.set_game_status(True)

        else:
            return False


    def move_left(self) -> None:
        
        """Move the ball left until it hits the left border. Bounces back 
        from the left border of the gameboard rightwards."""

        self.x_velocity = - 1

        self.gameboard.move(self.ball, self.x_velocity, 0)
     
        if self.handle_gameborder_collision():
            self.move_right()

        else:
            self.gameboard.after(self.speed, self.move_left)


    def move_right(self) -> None:
        
        """Move the ball right until it hits the right border. Bounces back 
        from the right border of the gameboard leftwards."""

        self.x_velocity = 1
        self.gameboard.move(self.ball, self.x_velocity, 0)

        if self.handle_gameborder_collision():
            self.move_left()
        
        else:
            self.gameboard.after(self.speed, self.move_right)


    def move_up(self) -> None:
        
        """Move the ball up until it hits the topmost border. Bounces back 
        from the border of the gameboard downwards."""

        self.y_velocity = -1
        self.gameboard.move(self.ball, 0, self.y_velocity)

        if self.handle_gameborder_collision():
            self.move_down()

        else:
            self.gameboard.after(self.speed, self.move_up)


    def move_down(self) -> None:
        
        """Move the ball down until it hits either the plank and bounces back
        or it hits the border. If it hits the lower boundary, the game is over."""

        self.y_velocity = 1
        self.gameboard.move(self.ball, 0, self.y_velocity)

        if self.handle_ball_plank_collision():
            self.move_up()

        elif self.gameboard.game_is_lost():
          
            self.x_velocity, self.y_velocity = 0, 0
            self.gameboard.delete(self.ball)
            self.gameboard.scoreboard.lost_game()

        else:
            self.gameboard.after(self.speed, self.move_down)
        
