from random import randrange
from GameObjects.GameItem import GameItem
from Settings.Settings import COLOURS, PLANK_SIZE


class Plank(GameItem):
    
    def __init__(self, game_board_object: object, speed: int) -> None:
        super().__init__(game_board_object, speed)
        self.gameboard = game_board_object
        self.colour = COLOURS[randrange(0, len(COLOURS) - 1)]
        self.SPEED = speed
        # self.start_x= self.gameboard.gameboard_width // 2
        # self.start_y= self.gameboard.gameboard_height
        self.x_velocity = 0
        self.y_velocity = 0
        self.after_id = None


    def create_plank(self, left_edge_coord: int, upper_edge_coord: int) -> None:
        """Initialization of the plank item"""
        colour= self.colour
        right_edge_coord = left_edge_coord - 20 - PLANK_SIZE
        lower_edge_coord = upper_edge_coord - 10
        self.plank = self.gameboard.create_rectangle(left_edge_coord, upper_edge_coord, right_edge_coord, lower_edge_coord, fill= colour)
   

    def handle_collision(self) -> None:
        """Handles collision of the plank"""

        #right border of game
        if self.gameboard.get_coords(self.plank)[2] >= self.gameboard.get_width():
            return True

        #left border of game
        elif self.gameboard.get_coords(self.plank)[0] <= 2:
            return True


    def move_left(self) -> None:
        """Move left until the plank hits the left border"""

        self.x = -1
        self.gameboard.move(self.plank, self.x, 0)
        
        if self.after_id != None:
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
        
        if self.after_id != None:
            self.gameboard.after_cancel(self.after_id)

        if self.handle_collision():
            self.x_velocity = -1
            self.gameboard.move(self.plank, self.x_velocity, 0)
            self.gameboard.after_cancel(self.after_id)

        else:
            self.after_id = self.gameboard.after(self.SPEED, self.move_right)
