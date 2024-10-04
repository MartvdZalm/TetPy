import random

class Shape:
    def __init__(self, shape):
        self.shape = shape
        self.color = "black"
        self.x = 0
        self.y = 0
        self.shapes = []
        self.current_rotation = 0

        self.init_shapes()

    def init_shapes(self):
        self.shapes = []

        for _ in range(4):
            r = len(self.shape[0])
            c = len(self.shape)

            rotated_shape = [[0] * c for _ in range(r)]

            for y in range(r):
                for x in range(c):
                    rotated_shape[y][x] = self.shape[c - x - 1][y]

            self.shapes.append(rotated_shape)
            self.shape = rotated_shape

    def spawn(self, grid_width):
        self.current_rotation = random.randint(0, len(self.shapes) - 1)
        self.shape = self.shapes[self.current_rotation]

        self.y = -self.get_height()
        self.x = random.randint(0, grid_width - self.get_width())
        self.color = self.get_color()

    def get_shape(self):
        return self.shape

    def get_color(self):
        return self.color

    def get_height(self):
        return len(self.shape)

    def get_width(self):
        return len(self.shape[0])

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def rotate(self):
        self.current_rotation = (self.current_rotation + 1) % 4
        self.shape = self.shapes[self.current_rotation]

    def get_bottom_edge(self):
        return self.y + self.get_height()

    def get_left_edge(self):
        return self.x

    def get_right_edge(self):
        return self.x + self.get_width()