from .Shape import Shape

class JShape(Shape):
    def __init__(self):
        super().__init__([[0, 1], [0, 1], [1, 1]])
        self.color = "blue"