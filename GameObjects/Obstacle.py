
from GameObjects.GameItem import GameItem
from random import randrange

from Settings.Settings import COLOURS

class Obstacle(GameItem):
    """Obstacles with different values as points. Can be destroyed to 
    gather points and climb in score."""
    
    def __init__(self, GameBoard: object) -> None:
        super().__init__(GameBoard)
        self.destroyed = False
        self.score_value = 0
        # self.colour_list ={"red", "green", "blue", "grey"}
        self.colour = COLOURS[randrange[0, len(COLOURS) - 1]]


    def create_obstacle(self) -> None:
        self.obstacle = self.gameboard.canvasItem.create_rectangle(20, 20, 30, 30, fill=self.colour)


    def destroy_obstacle(self) -> None:
        self.destroyed = True

    
    def get_obstacle_value(self) -> int:
        return self.score_value
    