
TITLE: str = "PYTHON PONG"
SCORE_VALUE: int = 1
COLOURS: list[str] = ["red", "green", "blue", "grey", "yellow", "purple", "white", "black", "lightgreen", "brown", "pink"]
FRAME_BORDERWIDTH: int = 6
GAMEBOARD_WIDTH: int = 400
GAMEBOARD_HEIGTH: int = 400
MODULO_FOR_DIFFICULTY: int = 10 # lower value == higher difficulty
PLANK_SIZE_REDUCTION: int = 5 # higher value = higher difficulty, since plank size decreases more

### Plank Constants
PLANK_SPEED: int = 5  # higher value is slower and thus harder
PLANK_SIZE: int = GAMEBOARD_WIDTH // 4  # lower value = bigger plank
PLANK_TAG: str = "plank"
MIN_PLANK_SIZE: int = 20

### Ball Constants
BALL_SPEED: int = 5  # higher value is slower and thus easier
BALL_SIZE: int = 10
BALL_TAG: str = "ball"
### Obstacle Constants