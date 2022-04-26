from GameItem import GameItem


class Plank(GameItem):
    
    def __init__(self, GameBoardObject: object, speed: int = 4, colour: str = "green") -> None:
        super().__init__(GameBoardObject, speed)
        self.colour = colour
        self.SPEED = speed
        self.start_x, self.start_y = self.gameboard.WIDTH, self.gameboard.HEIGHT
        self.x = 0
        self.y = 0


    def create_plank(self) -> None:
        """Initialization of the plank item"""
        
        self.plank = self.gameboard.canvasItem.create_rectangle(self.start_x - 20, self.start_y - 20, self.start_x - 95, self.start_y - 30, fill=self.colour)


    def handle_collision(self) -> None:
        """Handles collision of the plank"""

        #right border of game
        if self.get_coords(self.plank)[2] >= self.gameboard.get_width():
            return True

        #left border of game
        elif self.get_coords(self.plank)[0] < 1:
            return True


    def move_left(self) -> None:
        """Move left until the plank hits the most left border"""
       
        self.x = -1
        self.gameboard.canvasItem.move(self.plank, self.x, 0)
        
        if self.handle_collision():
            self.x = 1
            self.gameboard.canvasItem.move(self.plank, self.x, 0)

        else:
            self.gameboard.canvasItem.after(self.SPEED, self.move_left)


    def move_right(self) -> None:
        """Move right until the plank hits the most right border"""
        
        self.x = 1
        self.gameboard.canvasItem.move(self.plank, self.x, 0)
        
        if self.handle_collision():
            self.x = -1
            self.gameboard.canvasItem.move(self.plank, self.x, 0)
        
        else:
            self.gameboard.canvasItem.after(self.SPEED, self.move_right)
    