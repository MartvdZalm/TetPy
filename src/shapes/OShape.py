from .Shape import Shape

class OShape(Shape):
    def __init__(self):
        super().__init__([[1, 1], [1, 1]])
        self.color = "yellow"