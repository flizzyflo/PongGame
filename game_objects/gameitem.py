

from abc import abstractmethod, ABC


class GameItem(ABC):
    
    """Abstract class for the game items like ball or plank. 
    Provides some methods which can be used to navigate on the canvas."""

    def __init__(self, game_board_object: 'GameBoard', object_speed: int) -> None:
        self.gameboard = game_board_object
        self.speed = object_speed
    
    def set_speed(self, speed: int) -> None:

        """
        Set speed of the 'after' method. Can be used to adjust difficulty.
        """

        self.speed = speed

    @abstractmethod
    def move_left(self) -> None:
        pass

    @abstractmethod
    def move_right(self) -> None:
        pass

    @abstractmethod
    def move_up(self) -> None:
        pass

    @abstractmethod
    def move_down(self) -> None:
        pass
