from GameItem import GameItem

class Plank(GameItem):
    
    def __init__(self, GameBoardObject: object, speed: int = 4, colour: str = "green"):
        super().__init__(GameBoardObject)
        self.colour = colour
        self.SPEED = speed
        self.start_x, self.start_y = self.gameboard.WIDTH, self.gameboard.HEIGHT


    def create_plank(self) -> None:
        """Initialization of the plank item"""
        
        self.plank = self.gameboard.canvasItem.create_rectangle(self.start_x - 10, self.start_y - 10, self.start_x - 85, self.start_y - 20, fill=self.colour)


    def move_left(self):
        """Move left until the plank hits the most left border"""

        self.gameboard.canvasItem.move(self.plank, -1, 0)
        x1_coord = self.get_coords(self.plank)[0]

        if x1_coord < 1:
            self.gameboard.canvasItem.move(self.plank, 0, 0)

        else:
            self.gameboard.canvasItem.after(self.SPEED, self.move_left)


    def move_right(self):
        """Move right until the plank hits the most right border"""

        self.gameboard.canvasItem.move(self.plank, 1, 0)
        x2_coord= self.get_coords(self.plank)[2]

        if x2_coord >= self.gameboard.get_width():
            self.gameboard.canvasItem.move(self.plank, 0, 0)
        
        else:
            self.gameboard.canvasItem.after(self.SPEED, self.move_right)
    