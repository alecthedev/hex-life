from random import randint
from tkinter import Canvas, Tk

from hex import HexManager
from vector2 import Vector2

WIDTH, HEIGHT = 1200, 850

root = Tk()
root.title("Hex Life - github.com/alecthedev")
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

num = randint(0, 999)
print(num)

hex_manager = HexManager(Vector2(WIDTH // 2, HEIGHT // 2), 4, 70, canvas, seed=None)
root.bind("<Return>", hex_manager.toggle_running)

root.mainloop()
