from tkinter import Canvas, Tk

from hex import HexManager
from vector2 import Vector2

WIDTH, HEIGHT = 1200, 850

root = Tk()
root.title("Hex Life - github.com/alecthedev")
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

hex_manager = HexManager(Vector2(WIDTH // 2, HEIGHT // 2), 12, 20, canvas, seed=5)
root.bind("<Return>", hex_manager.update_world)

root.mainloop()
