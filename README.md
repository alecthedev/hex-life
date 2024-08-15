# Hex Life - Cellular Automata Simulation
A variation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) in Python3 using hexagonal tiles

![all_patterns 2](https://github.com/user-attachments/assets/acd61ddf-9584-432c-a224-dc302d63c5d8)


See the _[Getting Started](https://github.com/alecthedev/hex-life?tab=readme-ov-file#getting-started)_ section below if you would like to try the simulation out for yourself.

---

## How it works

Each cell has 2 possible states, dead (black) or alive (green).

The state of each cell is determined by its state in the previous generation, combined with the states of its neighbors.
Neighbors, in this case, are adjacent cells only.

Each generation checks the following conditions:

1. A live cell dies if it has fewer than 3 live neighbors
2. A live cell continues to the next generation if it has exactly 3 live neighbors
3. A live cell dies if it has 4 or more neighbors
4. A dead cell becomes alive if it has exactly 2 neighbors.

These conditions differ slightly from the original rules, as I adapted them for hexagonal cells and coordinates.

---

## Features and Demos

Left-click to set a cell to "alive", Right-click to set cell to "dead".

![clicking](https://github.com/user-attachments/assets/4c5d7558-d893-404b-917c-08977f5a193e)

Speed controls + Play/Pause the simulation. Manual step to next generation.

![controls](https://github.com/user-attachments/assets/ee5fc590-893f-48bf-afad-357f15cb5f18)

Randomize the world / Reset to all dead cells. Change the world size.

![settings](https://github.com/user-attachments/assets/17bb2fbe-864b-40d3-8996-66aee53a360b)

---

## Examples of some patterns

Currently, I am not aware of any "still lifes" as found within the original version. I have found several oscillators however.

Some of these were discovered occurring naturally/from static. Others were first seen when playing around with the drawing feature and trying to create repeating patterns on purpose.

I did not include all rotations of each oscillator.

| **Period 2** |                      |
| ------------ | -------------------- |
| Blinker      |  ![blinker 1](https://github.com/user-attachments/assets/e026ec2a-f12b-41b1-ad87-e1de21dacdeb) |
| Dancer       | ![dancer](https://github.com/user-attachments/assets/facbf688-75fe-4a27-bf17-19dbe6f07138) |
| Tri-Blinker  | ![tri-blinker](https://github.com/user-attachments/assets/5fdf05a6-79fe-4d0d-9fe9-3cbe3f89802d) |  
| Tri-Dancer   | ![tri-dancer](https://github.com/user-attachments/assets/8161ab18-6447-40bb-8c22-f3174cbf3000) |
| Quad-Dancer  | ![quad-dancer](https://github.com/user-attachments/assets/031bda7e-9ddf-4311-96f1-6a02e586743f) |

| **Period 3** |                      |
| ------------ | -------------------- |
| Hex-Blinker  | ![hex-blinker](https://github.com/user-attachments/assets/2abeec16-53d0-445f-861d-a310010e69a5) |

| **Period 4** |                     |
| ------------ | ------------------- |
| Jumper       | ![jumper](https://github.com/user-attachments/assets/d14479be-7dea-425f-8348-e7e481d7596c) |
| Big-Dancer   | ![big-dancer](https://github.com/user-attachments/assets/e42e5c55-0a5e-43af-995f-7fbbb50f1e6b) |

| **Period 10** |              |
| ------------- | ------------ |
| Trefoil       |  ![trefoil](https://github.com/user-attachments/assets/9fc8b92b-93cc-43f0-a826-cfbfb6ba068e) |


| **Period 12** |              |
| ------------- | ------------ |
| Koi           | ![koi](https://github.com/user-attachments/assets/1e72a036-6f2d-476c-b179-e70b8ada390c) |

| **Period 15** |                   |
| ------------- | ----------------- |
| Firework      | ![firework](https://github.com/user-attachments/assets/061b41a3-beea-4186-b069-dc7813d6968b) |

---

## Getting Started

### Prerequisites:
- Knowledge of basic [CLI](https://en.wikipedia.org/wiki/Command-line_interface) usage
- [Python3](https://www.python.org/downloads/) (download page on python.org)
- Tkinter:
    - When installing Python check "tcl/tk and IDLE" under optional features

#### 1. Clone this repository
```shell
git clone https://github.com/alecthedev/hex-life.git
cd hex-life
```

#### 2. Execute 'run.sh' to Start Program
```shell
./run.sh
```

#### 3. Enjoy!

If you happen to use this program and discover any new patterns please don't hesitate to contact me! I would love to add new 'creatures' to the catalog.

For example, I discovered 'trefoil' a week after recording the others!

