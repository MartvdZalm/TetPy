from .Shape import Shape

class LShape(Shape):
    def __init__(self):
        super().__init__([[1, 0], [1, 0], [1, 1]])
        self.color = "orange"