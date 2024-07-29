from tkinter import Canvas, Tk

from hex import Hex, HexManager
from vector2 import Vector2

WIDTH, HEIGHT = 800, 450

root = Tk()
root.title("Hex Life - github.com/alecthedev")
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

hex_manager = HexManager(Vector2(WIDTH // 2, HEIGHT // 2), 5, 25, canvas)

root.mainloop()
