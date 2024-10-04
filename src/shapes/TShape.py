from .Shape import Shape

class TShape(Shape):
    def __init__(self):
        super().__init__([[1, 1, 1], [0, 1, 0]])
        self.color = "magenta"