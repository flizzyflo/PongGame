
from Settings.Settings import TITLE
from tkinter import Tk

class MainWindow(Tk):

    def __init__(self) -> None:
        super().__init__()
        self.title = TITLE
