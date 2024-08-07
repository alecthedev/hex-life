from tkinter import Canvas, Tk, ttk

from hex import HexManager
from vector2 import Vector2

print("Launching Simulation...")


WIDTH, HEIGHT = 1000, 875

world_sizes = {
    "small": (15, 18),
    "medium": (10, 28),
    "large": (7, 40),
    "huge": (4, 70),
}

curr_world_size = world_sizes["medium"]

# create window and frames
root = Tk()
root.title("Hex Life - github.com/alecthedev")
root.resizable(False, False)
content = ttk.Frame(root)
options = ttk.Frame(root)

controls = ttk.Frame(options, padding=(0, 100))
settings = ttk.Frame(options, padding=(0, 100))

# canvas for drawing and simulation manager
canvas = Canvas(content, width=WIDTH, height=HEIGHT, bg="black")

hex_manager = HexManager(
    Vector2(WIDTH // 2, HEIGHT // 2), curr_world_size[0], curr_world_size[1], canvas
)

generation_label = ttk.Label(root, text=f"Generation: {hex_manager.generation}")
instructions = ttk.Label(
    options,
    text="""
    Welcome to Hex Life!


    Left-click to Add Cell

    Right-click to Remove
""",
)

# control frame buttons and labels
controls_label = ttk.Label(controls, text="Controls", padding=(0, 20))
play_pause_button = ttk.Button(
    controls, text="Play/Pause", command=hex_manager.toggle_running
)
step_button = ttk.Button(controls, text="Next Gen", command=hex_manager.update_world)
speed_inc_button = ttk.Button(
    controls,
    text="Speed +",
)
speed_dec_button = ttk.Button(
    controls,
    text="Speed −",
)

# settings frame buttons and labels
settings_label = ttk.Label(settings, text="Settings", padding=(0, 20))
reset_button = ttk.Button(settings, text="Reset World", command=hex_manager.reset_world)
randomize_button = ttk.Button(
    settings, text="Randomize", command=hex_manager.seed_world
)

# root grid
content.grid(column=0, row=1, columnspan=2)
options.grid(column=2, row=1, columnspan=1, padx=15)
generation_label.grid(column=0, row=2, columnspan=2)

# content frame grid
canvas.grid(column=0, row=0, padx=15)

# option frame grid
instructions.grid(column=0, row=0)
controls.grid(column=0, row=3)
settings.grid(column=0, row=5)

# control frame grid
controls_label.grid(column=0, row=0, columnspan=2)
play_pause_button.grid(column=0, row=1)
step_button.grid(column=1, row=1)
speed_dec_button.grid(column=0, row=2)
speed_inc_button.grid(column=1, row=2)

# settings frame grid
settings_label.grid(column=0, row=0, columnspan=2)
reset_button.grid(column=0, row=1)
randomize_button.grid(column=1, row=1)

root.bind("<Return>", hex_manager.update_world)


def update_labels():
    generation_label.config(text=f"Generation: {hex_manager.generation}")
    root.after(5, update_labels)


update_labels()

root.mainloop()


print("Exiting...")
