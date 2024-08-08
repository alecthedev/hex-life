import random as rand
from math import cos, pi, sin, sqrt

from vector2 import Vector2


class Hex:
    def __init__(self, q, r, s, canvas=None, size=25, origin=Vector2(0, 0)) -> None:
        self.q, self.r, self.s = q, r, s
        assert self.q + self.r + self.s == 0
        self.size = size
        self.center = hex_to_pixel(q, r, size, origin)
        self.canvas = canvas
        self.vertices = self.calc_vertices()
        self.live_neighbors = 0
        self.state = 0
        self.next_state = 0
        self.state_changed = False

    def __repr__(self) -> str:
        return f"Hex at ({self.q},{self.r},{self.s}), state: {self.state}"

    def check_state(self):
        old_state = self.state
        self.next_state = self.state
        # only check if alive
        if self.state == 1:
            # rule 1: A live cell dies if fewer than 3 live neighbors
            if self.live_neighbors < 3:
                self.next_state = 0

            # rule 2: A live cell continues if 3 live neighbors

            # rule 3: A live cell dies if 4 or more live neighbors
            if self.live_neighbors >= 4:
                self.next_state = 0

        # only check if dead
        else:
            # rule 4: A dead cell becomes live if exactly 2 live neighbors
            if self.live_neighbors == 2:
                self.next_state = 1
        if old_state != self.next_state:
            # state changed
            self.state_changed = True

    def update_state(self):
        if self.state_changed:
            self.state = self.next_state
            self.state_changed = False
            self.draw()

    def calc_vertices(self):
        vertices = []
        for i in range(6):
            offset = self.calc_vertex_offset(i)
            vertices.append(Vector2(self.center.x, self.center.y) + offset)
        return vertices

    def calc_vertex_offset(self, vertex: int):
        angle = 2 * pi * (vertex + 0.5) / 6
        return Vector2(self.size * cos(angle), self.size * sin(angle))

    def draw(self):
        assert self.canvas is not None
        color = "#0e802a"
        if self.state == 0:
            color = "black"
        points = []
        for v in self.vertices:
            points.append(v.x)
            points.append(v.y)
        self.canvas.create_polygon(
            points,
            fill=color,
            outline="grey10",
            # outline="black",
            activefill="#243a2a",
            width=self.size // 3,
        )


class HexManager:
    def __init__(self, origin: Vector2, canvas):
        self.origin = origin
        self.canvas = canvas
        self.hexes = {}
        self.generation = 0
        self.running = False

        self.world_sizes = {  # (hex_size, world_size)
            "small": (15, 18),
            "medium": (10, 28),
            "large": (7, 40),
            "huge": (4, 70),
        }
        self.curr_size = self.world_sizes["medium"]
        self.hex_size = self.curr_size[0]
        self.world_size = self.curr_size[1]

        self.speeds = {  # determines update_world freq in millisec
            "slow": 750,
            "normal": 200,
            "fast": 100,
            "faster": 50,
        }
        self.curr_speed = self.speeds["normal"]

        self.generate_world()

        self.canvas.bind(
            "<Button-1>", lambda event, state=1: self.set_hex_state(event, state)
        )
        self.canvas.bind(
            "<B1-Motion>", lambda event, state=1: self.set_hex_state(event, state)
        )
        self.canvas.bind(
            "<Button-3>", lambda event, state=0: self.set_hex_state(event, state)
        )
        self.canvas.bind(
            "<B3-Motion>", lambda event, state=0: self.set_hex_state(event, state)
        )

    def update_speed(self, increasing: bool):
        if self.curr_speed == self.speeds["slow"]:
            if increasing:
                self.curr_speed = self.speeds["normal"]
            else:
                return
        elif self.curr_speed == self.speeds["normal"]:
            if increasing:
                self.curr_speed = self.speeds["fast"]
            else:
                self.curr_speed = self.speeds["slow"]
        elif self.curr_speed == self.speeds["fast"]:
            if increasing:
                self.curr_speed = self.speeds["faster"]
            else:
                self.curr_speed = self.speeds["normal"]
        elif self.curr_speed == self.speeds["faster"]:
            if increasing:
                return
            else:
                self.curr_speed = self.speeds["fast"]

    def update_size(self, increasing: bool):
        if self.curr_size == self.world_sizes["small"]:
            if increasing:
                self.curr_size = self.world_sizes["medium"]
            else:
                return
        elif self.curr_size == self.world_sizes["medium"]:
            if increasing:
                self.curr_size = self.world_sizes["large"]
            else:
                self.curr_size = self.world_sizes["small"]
        elif self.curr_size == self.world_sizes["large"]:
            if increasing:
                self.curr_size = self.world_sizes["huge"]
            else:
                self.curr_size = self.world_sizes["medium"]
        elif self.curr_size == self.world_sizes["huge"]:
            if increasing:
                return
            else:
                self.curr_size = self.world_sizes["large"]

        self.hex_size = self.curr_size[0]
        self.world_size = self.curr_size[1]
        self.reset_world()

    def update_world(self, event=None):
        # while self.running:
        # update neighbors for each cell
        for hex in self.hexes.values():
            hex.live_neighbors = self.get_live_neighbors(hex)
        # check rules for each AFTER updating their live neighbor count
        for hex in self.hexes.values():
            hex.check_state()
        # update state for each hex based on rules checked last loop
        for hex in self.hexes.values():
            hex.update_state()

        self.animate()
        self.generation += 1

        if self.running and event is None:
            self.canvas.after(self.curr_speed, self.update_world)

    def reset_world(self, event=None):
        self.canvas.create_rectangle(
            0, 0, self.canvas.winfo_width(), self.canvas.winfo_height(), fill="black"
        )
        self.running = False
        self.generation = 0
        self.hexes = {}
        self.generate_world()
        self.animate()

    def get_live_neighbors(self, hex):
        live_neighbors = 0
        for dir in hex_directions:
            n_q = hex.q + dir.q
            n_r = hex.r + dir.r
            n_s = hex.s + dir.s
            n_pos = (n_q, n_r, n_s)
            if self.check_neighbor_exists(n_pos):
                # append only if alive
                if self.hexes[n_pos].state == 1:
                    live_neighbors += 1
        return live_neighbors

    def check_neighbor_exists(self, hex_pos):
        return hex_pos in self.hexes

    def seed_world(self, event=None):
        self.reset_world()
        num_alive = 0
        for hex in self.hexes.values():
            if rand.randint(1, 3) == 1:
                hex.state = 1
                hex.draw()
                # self.animate()
                num_alive += 1
                if num_alive >= len(self.hexes) // 5:
                    return

    def generate_world(self):
        self.calc_spiral()
        self.draw_spiral()

    def calc_spiral(self):
        q, r, s = 0, 0, 0
        self.hexes[(q, r, s)] = Hex(q, r, s, self.canvas, self.hex_size, self.origin)
        for ring in range(self.world_size + 1):
            q, r, s = -ring, ring, 0
            for dir in hex_directions:
                for _ in range(ring):
                    q += dir.q
                    r += dir.r
                    s += dir.s
                    self.hexes[(q, r, s)] = Hex(
                        q, r, s, self.canvas, self.hex_size, self.origin
                    )

    def draw_spiral(self):
        for hex in self.hexes.values():
            hex.draw()

    def animate(self):
        self.canvas.update()
        self.canvas.update_idletasks()

    def toggle_running(self, event=None):
        self.running = not self.running
        if self.running:
            self.update_world()

    def set_hex_state(self, event, state):
        click_pos = pixel_to_hex(self.hex_size, Vector2(event.x, event.y) - self.origin)
        clicked_hex = None
        if (click_pos) in self.hexes:
            clicked_hex = self.hexes[(click_pos)]

        if clicked_hex is not None and state != clicked_hex.state:
            clicked_hex.state = state
            clicked_hex.draw()


def pixel_to_hex(hex_size, vector: Vector2):
    q = (sqrt(3) / 3 * vector.x - 1 / 3 * vector.y) / hex_size
    r = (2 / 3 * vector.y) / hex_size
    return round_hex(q, r, -q - r)


def hex_to_pixel(q, r, size, origin):
    x = size * (sqrt(3) * q + sqrt(3) / 2 * r) + origin.x
    y = size * (3 / 2 * r) + origin.y
    return Vector2(x, y)


def round_hex(frac_q, frac_r, frac_s):
    q = round(frac_q)
    r = round(frac_r)
    s = round(frac_s)

    q_diff = abs(q - frac_q)
    r_diff = abs(r - frac_r)
    s_diff = abs(s - frac_s)

    if q_diff > r_diff and q_diff > s_diff:
        q = -r - s
    elif r_diff > s_diff:
        r = -q - s
    else:
        s = -q - r

    return q, r, s


hex_directions = [
    Hex(1, 0, -1),  # E
    Hex(1, -1, 0),  # NE
    Hex(0, -1, 1),  # NW
    Hex(-1, 0, 1),  # W
    Hex(-1, 1, 0),  # SW
    Hex(0, 1, -1),  # SE
]
