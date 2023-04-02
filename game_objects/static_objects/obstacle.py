
from random import randrange
from typing import Self

from settings.settings import COLOURS


class Obstacle:
    """
    Obstacles with different values as points. Can be destroyed to
    gather points and climb in score.
    """

    existing_obstacles: set[Self] = set()

    def __init__(self, game_board_object: 'GameBoard') -> None:
        self.gameboard = game_board_object
        self.destroyed = False
        self.score_value = 0
        self.colour = COLOURS[randrange(0, len(COLOURS) - 1)]
        self.obstacle = None

    def create_obstacle(self, coordinates: tuple[int]) -> None:
        self.obstacle = self.gameboard.create_rectangle(coordinates, fill="red", tags=self)
        Obstacle.existing_obstacles.add(self.obstacle)

    def get_coordinates(self):
        return self.obstacle

    def destroy_obstacle(self) -> None:
        Obstacle.existing_obstacles.remove(self)
        self.gameboard.delete(self)

    def get_value(self) -> int:
        return self.score_value

    def set_score_value(self, score_value: int) -> None:
        self.score_value = score_value
