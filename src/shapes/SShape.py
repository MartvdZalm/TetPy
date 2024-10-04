from .Shape import Shape

class SShape(Shape):
    def __init__(self):
        super().__init__([[0, 1, 1], [1, 1, 0]])
        self.color = "green"