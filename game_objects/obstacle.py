
from random import randrange

from settings.settings import COLOURS


class Obstacle:
    """
    Obstacles with different values as points. Can be destroyed to
    gather points and climb in score.
    """

    def __init__(self, game_board_object: 'GameBoard', object_speed: int) -> None:
        self.gameboard = game_board_object
        self.speed = object_speed
        self.destroyed = False
        self.score_value = 0
        # self.colour_list ={"red", "green", "blue", "grey"}
        self.colour = COLOURS[randrange[0, len(COLOURS) - 1]]

    def create_obstacle(self) -> None:
        ...

    def destroy_obstacle(self) -> None:
        ...

    def get_obstacle_value(self) -> int:
        ...
