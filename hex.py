import random as rand
from math import cos, pi, sin, sqrt
from time import sleep

from vector2 import Vector2


class Hex:
    def __init__(self, q, r, s, canvas=None, size=25, origin=Vector2(0, 0)) -> None:
        self.q, self.r, self.s = q, r, s
        assert self.q + self.r + self.s == 0
        self.size = size
        self.center = hex_to_pixel(q, r, size, origin)
        self.canvas = canvas
        self.vertices = []
        self.live_neighbors = 0
        self.state = 0

    def __repr__(self) -> str:
        return f"Hex at ({self.q},{self.r},{self.s}), state: {self.state}"

    def update(self):
        if self.state == 1:
            # only check if alive
            self.check_rule_1()
            self.check_rule_2()
            self.check_rule_3()
        else:
            # only check if dead
            self.check_rule_4()

    def check_rule_1(self):
        # rule 1: A live cell dies if fewer than 2 live neighbors
        pass

    def check_rule_2(self):
        # rule 2: A live cell continues if 2 to 3 live neighbors
        pass

    def check_rule_3(self):
        # rule 3: A live cell dies if greater than 3 live neighbors
        pass

    def check_rule_4(self):
        # rule 4: A dead cell becomes live if exactly 3 live neighbors
        pass

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
        self.vertices = self.calc_vertices()
        points = []
        for v in self.vertices:
            points.append(v.x)
            points.append(v.y)
        self.canvas.create_polygon(
            points,
            fill=color,
            outline="grey10",
            # outline="black",
            width=self.size // 3,
        )


class HexManager:
    def __init__(
        self, origin: Vector2, hex_size: int, world_size: int, canvas, seed=None
    ):
        self.origin = origin
        self.hex_size = hex_size
        self.world_size = world_size
        self.canvas = canvas
        self.hexes = {}
        self.generation = 0

        if seed:
            rand.seed(seed)

        self.generate_world()
        self.seed_world()
        self.update_world()

    def update_world(self):
        # update neighbors for each cell
        for hex in self.hexes.values():
            hex.live_neighbors = self.get_live_neighbors(hex)
        # check rules for each AFTER updating their neighbors
        for hex in self.hexes.values():
            hex.update()
            hex.draw()

        # draw each cell
        self.animate()
        self.generation += 1

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

    def seed_world(self):
        num_alive = 0
        while num_alive < len(self.hexes) // 10:
            for hex in self.hexes.values():
                if rand.randint(0, 10) == 0:
                    hex.state = 1
                    hex.draw()
                    num_alive += 1

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
            self.animate()

    def animate(self):
        self.canvas.update()
        self.canvas.update_idletasks()


def pixel_to_hex(hex: Hex, vector: Vector2):
    q = (sqrt(3) / 3 * vector.x - 1 / 3 * vector.y) / hex.size
    r = (2 / 3 * vector.y) / hex.size
    return q, r, -q - r


def hex_to_pixel(q, r, size, origin):
    x = size * (sqrt(3) * q + sqrt(3) / 2 * r) + origin.x
    y = size * (3 / 2 * r) + origin.y
    return Vector2(x, y)


hex_directions = [
    Hex(1, 0, -1),  # E
    Hex(1, -1, 0),  # NE
    Hex(0, -1, 1),  # NW
    Hex(-1, 0, 1),  # W
    Hex(-1, 1, 0),  # SW
    Hex(0, 1, -1),  # SE
]
