from random import randint
from tkinter import Canvas, Tk, ttk

from hex import HexManager
from vector2 import Vector2

print("Launching Simulation...")


WIDTH, HEIGHT = 1000, 875

# create window and frames
root = Tk()
root.title("Hex Life - github.com/alecthedev")
content = ttk.Frame(root)
controls = ttk.Frame(root)

# create canvas for drawing, create simulation manager
canvas = Canvas(content, width=WIDTH, height=HEIGHT, bg="black")
hex_manager = HexManager(Vector2(WIDTH // 2, HEIGHT // 2), 10, 28, canvas)

# create labels and buttons
generation_label = ttk.Label(content, text=f"Generation: {hex_manager.generation}")

play_pause_button = ttk.Button(
    controls, text="Play/Pause", command=hex_manager.toggle_running
)
reset_button = ttk.Button(controls, text="Reset World", command=hex_manager.reset_world)
randomize_button = ttk.Button(
    controls, text="Randomize World", command=hex_manager.seed_world
)

# add content items to grid
content.grid(column=0, row=0, columnspan=2)
canvas.grid(column=0, row=0)
generation_label.grid(column=0, row=1)

# add control items to grid
controls.grid(column=3, row=0, columnspan=1)
play_pause_button.grid(column=0, row=0)
reset_button.grid(column=0, row=1)
randomize_button.grid(column=0, row=2)

root.bind("<Return>", hex_manager.update_world)


def update_labels():
    generation_label.config(text=f"Generation: {hex_manager.generation}")
    root.after(5, update_labels)


update_labels()

root.mainloop()


print("Exiting...")
