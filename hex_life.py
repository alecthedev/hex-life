from tkinter import Canvas, Tk

from hex import Hex
from vector2 import Vector2

WIDTH, HEIGHT = 800, 450

root = Tk()
root.title("Hex Life - github.com/alecthedev")
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

hex = Hex(0, 0, 0, canvas, 100, Vector2(WIDTH // 2, HEIGHT // 2))
hex.draw()

root.mainloop()
