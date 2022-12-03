from random import randrange
from GameObjects.GameItem import GameItem
from Settings.Settings import COLOURS, PLANK_SPEED, PLANK_COLOUR


class Plank(GameItem):
    
    def __init__(self, GameBoardObject: object, speed: int, colour: str) -> None:
        super().__init__(GameBoardObject, speed)
        self.gameboard = GameBoardObject
        self.colour = COLOURS[randrange(0, len(COLOURS) - 1)]
        self.SPEED = speed
        self.start_x, self.start_y = self.gameboard.WIDTH // 2, self.gameboard.HEIGHT
        self.x = 0
        self.y = 0


    def create_plank(self) -> None:
        """Initialization of the plank item"""
        
        self.plank = self.gameboard.create_rectangle(self.start_x - 20, self.start_y - 20, self.start_x - 95, self.start_y - 30, fill=self.colour)


    def handle_collision(self) -> None:
        """Handles collision of the plank"""

        print(f"{self.x=}{self.y=}")
        #right border of game
        if self.get_coords(self.plank)[2] >= self.gameboard.get_width():
            return True

        #left border of game
        elif self.get_coords(self.plank)[0] < 1:
            return True


    def move_left(self) -> None:
        """Move left until the plank hits the left border"""

        self.x = -1
        self.gameboard.move(self.plank, self.x, 0)
        if self.handle_collision():
            self.x = 1
            self.gameboard.move(self.plank, self.x, 0)

        else:
            self.gameboard.after(self.SPEED, self.move_left)


    def move_right(self) -> None:
        """Move right until the plank hits the right border"""
        
        self.x = 1
        self.gameboard.move(self.plank, self.x, 0)
        if self.handle_collision():
            self.x = -1
            self.gameboard.move(self.plank, self.x, 0)
        
        else:
            self.gameboard.after(self.SPEED, self.move_right)
    
    