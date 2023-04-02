from random import randrange

from game_objects.moving_objects.gameitem import GameItem
from settings.settings import COLOURS, PLANK_SIZE, PLANK_TAG


class Plank(GameItem):
    
    """Plank class which represents the players object which is used to keep the ball in the game"""

    def __init__(self, game_board_object: 'GameBoard', speed: int) -> None:
        super().__init__(game_board_object, speed)
        self.plank = None
        self.SPEED = speed
        self.x_velocity = 0
        self.y_velocity = 0
        self.after_id = None
        self.x = None

    def create_plank(self, left_edge_coord: int, upper_edge_coord: int) -> None:
        
        """Initialization of the plank item"""
        
        plank_colour = COLOURS[randrange(0, len(COLOURS) - 1)]
        right_edge_coord = left_edge_coord - 20 - PLANK_SIZE
        lower_edge_coord = upper_edge_coord - 10
        self.plank = self.gameboard.create_rectangle(left_edge_coord, 
                                                     upper_edge_coord, 
                                                     right_edge_coord, 
                                                     lower_edge_coord, 
                                                     fill= plank_colour, 
                                                     tags= PLANK_TAG)
   
    def handle_collision(self) -> None:
        
        """Handles collision of the plank"""

        # right border of game
        if self.gameboard.get_gameboard_widget_coords(self.plank)[2] >= self.gameboard.get_width():
            return True

        # left border of game
        elif self.gameboard.get_gameboard_widget_coords(self.plank)[0] <= 2:
            return True

    def move_left(self) -> None:
        
        """Move left until the plank hits the left border"""

        self.x = -1
        self.gameboard.move(self.plank, self.x, 0)
        
        if self.after_id is not None:
            self.gameboard.after_cancel(self.after_id)

        if self.handle_collision():
            self.x_velocity = 1
            self.gameboard.move(self.plank, self.x_velocity, 0)

        else:
            self.after_id = self.gameboard.after(self.SPEED, self.move_left)

    def move_right(self) -> None:
        
        """Move right until the plank hits the right border"""
        
        self.x_velocity = 1
        self.gameboard.move(self.plank, self.x_velocity, 0)
        
        if self.after_id is not None:
            self.gameboard.after_cancel(self.after_id)

        if self.handle_collision():
            self.x_velocity = -1
            self.gameboard.move(self.plank, self.x_velocity, 0)
            self.gameboard.after_cancel(self.after_id)

        else:
            self.after_id = self.gameboard.after(self.SPEED, self.move_right)

    def move_up(self) -> None:
        ...

    def move_down(self) -> None:
        ...