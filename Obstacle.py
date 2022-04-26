
from GameItem import GameItem
from random import randrange

class Obstacle(GameItem):
    """Obstacles with different values as points. Can be destroyed to 
    gather points and climb in score."""
    
    def __init__(self, GameBoard: object) -> None:
        super().__init__(GameBoard)
        self.destroyed = False
        self.score_value = 0
        self.colour_list =["red", "green", "blue", "grey"]
        self.colour = self.colour_list[randrange[0, self.colour_list.length - 1]]

    def create_obstacle(self) -> None:
        self.obstacle = self.gameboard.canvasItem.create_rectangle(20, 20, 30, 30, fill=self.colour)

    def destroy_obstacle(self) -> None:
        self.destroyed = True

    