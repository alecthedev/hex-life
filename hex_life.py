from random import randint
from tkinter import Canvas, Tk, ttk

from hex import HexManager
from vector2 import Vector2

WIDTH, HEIGHT = 1200, 850


def build_sim():
    root = Tk()
    root.title("Hex Life - github.com/alecthedev")
    content = ttk.Frame(root)
    controls = ttk.Frame(root)

    canvas = Canvas(content, width=WIDTH, height=HEIGHT, bg="black")
    hex_manager = HexManager(Vector2(WIDTH // 2, HEIGHT // 2), 4, 70, canvas, seed=None)
    current_gen = hex_manager.generation

    generation_label = ttk.Label(content, text=f"Generation: {current_gen}")

    if current_gen != hex_manager.generation:
        current_gen = hex_manager.generation
        generation_label.setvar("text")

    play_pause_button = ttk.Button(
        controls, text="Play/Pause", command=hex_manager.toggle_running
    )
    reset_button = ttk.Button(
        controls, text="Reset World", command=hex_manager.reset_world
    )
    randomize_button = ttk.Button(
        controls, text="Randomize World", command=hex_manager.seed_world
    )

    content.grid(column=0, row=0, columnspan=2)
    canvas.grid(column=0, row=0)
    generation_label.grid(column=0, row=1)

    controls.grid(column=3, row=0, columnspan=1)
    play_pause_button.grid(column=0, row=0)
    reset_button.grid(column=0, row=1)
    randomize_button.grid(column=0, row=2)

    num = randint(0, 999)
    print(num)

    root.bind("<Return>", hex_manager.update_world)

    root.mainloop()


if __name__ == "__main__":
    print("Launching Simulation...")
    build_sim()
    print("Exiting...")
