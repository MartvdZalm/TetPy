import tkinter as tk
from GameFrame import GameFrame

def keypress(event):
    if event.char == "w":
        game_frame.rotate_block()

    if event.char == "s":
        game_frame.drop_block()

    if event.char == "a":
        game_frame.move_block_left()

    if event.char == "d":
        game_frame.move_block_right()

def main():
    global window, game_frame
    window.bind("<Key>", keypress)
    window.mainloop()

if __name__ == "__main__":
    window = tk.Tk()
    game_frame = GameFrame(window)
    main()