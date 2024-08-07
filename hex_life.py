from tkinter import Canvas, Tk, ttk

from hex import HexManager
from vector2 import Vector2

print("Launching Simulation...")


WIDTH, HEIGHT = 1000, 875

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

hex_manager = HexManager(Vector2(WIDTH // 2, HEIGHT // 2), canvas)

generation_label = ttk.Label(content, text=f"Generation: {hex_manager.generation}")
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
    controls, text="Speed +", command=hex_manager.increase_speed
)
speed_dec_button = ttk.Button(
    controls, text="Speed −", command=hex_manager.decrease_speed
)
speed_label_text = "Speed: █ █ _ _"
speed_label = ttk.Label(controls, text=speed_label_text)

# settings frame buttons and labels
settings_label = ttk.Label(settings, text="Settings", padding=(0, 20))
reset_button = ttk.Button(settings, text="Reset World", command=hex_manager.reset_world)
randomize_button = ttk.Button(
    settings, text="Randomize", command=hex_manager.seed_world
)
size_dec_button = ttk.Button(
    settings, text="World Size −", command=hex_manager.decrease_world_size
)
size_inc_button = ttk.Button(
    settings, text="World Size +", command=hex_manager.increase_world_size
)
size_label_text = "World Size: █ █ _ _"
size_label = ttk.Label(settings, text=size_label_text)

# root grid
content.grid(column=0, row=1, columnspan=2)
options.grid(column=2, row=1, columnspan=1, padx=15)

# content frame grid
canvas.grid(column=0, row=0, padx=15)
generation_label.grid(column=0, row=1, pady=30)

# option frame grid
instructions.grid(column=0, row=0)
controls.grid(column=0, row=3)
settings.grid(column=0, row=5)

# control frame grid
controls_label.grid(column=0, row=0, columnspan=2)
play_pause_button.grid(column=0, row=1)
step_button.grid(column=1, row=1)
speed_dec_button.grid(column=0, row=2, padx=5, pady=5)
speed_inc_button.grid(column=1, row=2, padx=5, pady=5)
speed_label.grid(column=0, row=3, columnspan=2, pady=15)

# settings frame grid
settings_label.grid(column=0, row=0, columnspan=2)
reset_button.grid(column=0, row=1)
randomize_button.grid(column=1, row=1)
size_dec_button.grid(column=0, row=2, padx=5, pady=5)
size_inc_button.grid(column=1, row=2, padx=5, pady=5)
size_label.grid(column=0, row=3, columnspan=2, pady=15)


def update_size_label():
    label = "Size: "
    if hex_manager.curr_size == hex_manager.world_sizes["small"]:
        label += "█ _ _ _"
    elif hex_manager.curr_size == hex_manager.world_sizes["medium"]:
        label += "█ █ _ _"
    elif hex_manager.curr_size == hex_manager.world_sizes["large"]:
        label += "█ █ █ _"
    else:
        label += "█ █ █ █"
    return label


def update_speed_label():
    label = "Speed: "
    if hex_manager.curr_speed == hex_manager.speeds["slow"]:
        label += "█ _ _ _"
    elif hex_manager.curr_speed == hex_manager.speeds["normal"]:
        label += "█ █ _ _"
    elif hex_manager.curr_speed == hex_manager.speeds["fast"]:
        label += "█ █ █ _"
    else:
        label += "█ █ █ █"
    return label


def update_labels():
    generation_label.config(text=f"Generation: {hex_manager.generation}")

    speed_label_text = update_speed_label()
    size_label_text = update_size_label()

    speed_label.config(text=speed_label_text)

    size_label.config(text=size_label_text)

    root.after(5, update_labels)


update_labels()

root.mainloop()


print("Exiting...")
