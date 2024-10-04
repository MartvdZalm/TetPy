import random
from tkinter import Canvas
from shapes import IShape, JShape, LShape, OShape, SShape, TShape, ZShape

class GameFrame:
    def __init__(self, window):
        self.screen_rows = 18
        self.screen_cols = 10
        self.tile_size = 40  # Set your tile size
        self.background = [[None for _ in range(self.screen_cols)] for _ in range(self.screen_rows)]
        self.block = None
        self.blocks = [IShape(), JShape(), LShape(), OShape(), SShape(), TShape(), ZShape()]

        self.canvas = Canvas(window, width=self.screen_cols * self.tile_size, height=self.screen_rows * self.tile_size)
        self.canvas.pack()
        self.canvas.configure(background='black')

        self.spawn_block()
        self.game_loop()

    def spawn_block(self):
        self.block = random.choice(self.blocks)
        self.block.spawn(self.screen_cols)

    def is_block_out_of_bounds(self):
        if self.block.get_bottom_edge() >= self.screen_rows:
            self.block = None
            return True
        return False

    def move_block_down(self):
        if not self.check_bottom():
            return False
        self.block.move_down()
        self.draw()
        return True

    def move_block_right(self):
        if self.block is None or not self.check_right():
            return
        self.block.move_right()
        self.draw()

    def move_block_left(self):
        if self.block is None or not self.check_left():
            return
        self.block.move_left()
        self.draw()

    def drop_block(self):
        if self.block is None:
            return
        while self.check_bottom():
            self.block.move_down()
        self.draw()

    def rotate_block(self):
        if self.block is None:
            return
        self.block.rotate()
        if self.block.get_left_edge() < 0:
            self.block.set_x(0)
        if self.block.get_right_edge() > self.screen_cols:
            self.block.set_x(self.screen_cols - self.block.get_width())
        if self.block.get_bottom_edge() >= self.screen_rows:
            self.block.set_y(self.screen_rows - self.block.get_height())
        self.draw()

    def check_bottom(self):
        if self.block.get_bottom_edge() == self.screen_rows:
            return False

        shape = self.block.get_shape()
        w = self.block.get_width()
        h = self.block.get_height()

        for col in range(w):
            for row in range(h - 1, -1, -1):
                if shape[row][col] != 0:
                    x = col + self.block.get_x()
                    y = row + self.block.get_y() + 1

                    if y < 0:
                        break
                    if self.background[y][x] is not None:
                        return False
                    break

        return True

    def check_left(self):
        if self.block.get_left_edge() == 0:
            return False

        shape = self.block.get_shape()
        w = self.block.get_width()
        h = self.block.get_height()

        for row in range(h):
            for col in range(w):
                if shape[row][col] != 0:
                    x = col + self.block.get_x() - 1
                    y = row + self.block.get_y()
                    if y < 0:
                        break
                    if self.background[y][x] is not None:
                        return False
                    break

        return True

    def check_right(self):
        if self.block.get_right_edge() == self.screen_cols:
            return False

        shape = self.block.get_shape()
        w = self.block.get_width()
        h = self.block.get_height()

        for row in range(h):
            for col in range(w - 1, -1, -1):
                if shape[row][col] != 0:
                    x = col + self.block.get_x() + 1
                    y = row + self.block.get_y()
                    if y < 0:
                        break
                    if self.background[y][x] is not None:
                        return False
                    break

        return True

    def clear_lines(self):
        for r in range(self.screen_rows - 1, -1, -1):
            if all(self.background[r][c] is not None for c in range(self.screen_cols)):
                self.clear_line(r)
                self.shift_down(r)

    def clear_line(self, r):
        for c in range(self.screen_cols):
            self.background[r][c] = None

    def shift_down(self, r):
        for row in range(r, 0, -1):
            for col in range(self.screen_cols):
                self.background[row][col] = self.background[row - 1][col]

    def move_block_to_background(self):
        shape = self.block.get_shape()
        h = self.block.get_height()
        w = self.block.get_width()
        xPos = self.block.get_x()
        yPos = self.block.get_y()
        color = self.block.get_color()

        for r in range(h):
            for c in range(w):
                if shape[r][c] == 1:
                    self.background[r + yPos][c + xPos] = color

    def draw_block(self):
        h = self.block.get_height()
        w = self.block.get_width()
        color = self.block.get_color()
        shape = self.block.get_shape()

        for row in range(h):
            for col in range(w):
                if shape[row][col] == 1:
                    x = (self.block.get_x() + col) * self.tile_size
                    y = (self.block.get_y() + row) * self.tile_size
                    self.draw_grid_square(color, x, y)

    def draw_background(self):
        for r in range(self.screen_rows):
            for c in range(self.screen_cols):
                color = self.background[r][c]
                if color is not None:
                    x = c * self.tile_size
                    y = r * self.tile_size
                    self.draw_grid_square(color, x, y)

    def draw_grid_square(self, color, x, y):
        self.canvas.create_rectangle(x, y, x + self.tile_size, y + self.tile_size, fill=color, outline="black")

    def draw(self):
        self.canvas.delete("all")
        self.draw_background()
        if self.block:
            self.draw_block()
        self.canvas.update()

    def game_loop(self):
        if self.move_block_down():
            self.draw()
        else:
            self.move_block_to_background()
            self.clear_lines()
            self.spawn_block()
            if self.is_block_out_of_bounds():
                print("Game Over")
                return
        self.canvas.after(250, self.game_loop)
