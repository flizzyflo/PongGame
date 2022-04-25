

from abc import abstractmethod

class GameItem:
    
    def __init__(self, GameBoardObject: object):
        self.gameboard = GameBoardObject
    
    def get_coords(self, GameObject: object) -> tuple[int]:
        """Returns the x1, y1, x2, y2 values of an object. Used to do collision calculation."""

        return self.gameboard.canvasItem.bbox(GameObject)

    def set_speed(self, speed: int) -> None:
        """Set speed of the 'after' method. Can be used to adjust difficulty later on."""

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