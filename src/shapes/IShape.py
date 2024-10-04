from .Shape import Shape

class IShape(Shape):
    def __init__(self):
        super().__init__([[1, 1, 1, 1]])
        self.color = "lightblue"