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
        self.neighbors = []
        self.state = 0

    def __repr__(self) -> str:
        return f"Hex at ({self.q},{self.r},{self.s}), state: {self.state}"

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
        color = "white"
        if self.state == 0:
            color = "black"
        self.vertices = self.calc_vertices()
        points = []
        for v in self.vertices:
            points.append(v.x)
            points.append(v.y)
        self.canvas.create_polygon(points, fill=color, outline="grey15")


class HexManager:
    def __init__(
        self, origin: Vector2, hex_size: int, world_size: int, canvas, seed=None
    ):
        self.origin = origin
        self.hex_size = hex_size
        self.world_size = world_size
        self.canvas = canvas
        self.hexes = {}

        if seed:
            rand.seed(seed)

        self.generate_world()

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
            self.draw_hex(hex)

    def draw_hex(self, hex):
        hex.draw()
        self.animate()

    def animate(self):
        sleep(0.005)
        self.canvas.update()


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
