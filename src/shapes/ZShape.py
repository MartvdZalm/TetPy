from .Shape import Shape

class ZShape(Shape):
    def __init__(self):
        super().__init__([[1, 1, 0], [0, 1, 1]])
        self.color = "red"
