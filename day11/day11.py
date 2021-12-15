from time import sleep
import copy

with open("input.txt", "r") as f:
    octopuses = [list(line) for line in f.read().strip().split('\n')]

og_octopuses = [[int(d) for d in line] for y, line in enumerate(octopuses)]

line_len = len(octopuses[0])
coord_map = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

flashes = 0
flashed = []

def print_octos(octopuses):
    global flashes

    to_print = "\033[;H"
    for line in octopuses:
        for nb in line:
            if nb == 0 or nb >= 10:
                to_print += "\033[1;0m0 "
            else:
                to_print += f"\033[1;35m{nb} "
        to_print += "\n"
    print(to_print)
    sleep(0.10)

def step(octopuses, steps, sync = False, show_octos = 0):
    global flashes

    if steps > 0 or sync:
        flashed = []
        for y, line in enumerate(octopuses):
            for x, octo in enumerate(line):
                octopuses[y][x] += 1
                if octo == 9:
                    flashed.append((x, y))
                    flashes += 1
        nb_flashed = update(octopuses, flashed, show_octos=show_octos)
        if show_octos == 1:
            print_octos(octopuses)
        if sync and nb_flashed == 100:
            print("Part 2:", steps)
            return steps
        if sync:
            step(octopuses, steps + 1, sync = True, show_octos=show_octos)
        else:
            step(octopuses, steps - 1, show_octos=show_octos)

def update(octopuses, flashed, show_octos = 0):
    global flashes

    for y, line in enumerate(octopuses):
        for x, octo in enumerate(line):
            if 0 < octo < 10:
                flashed_neighbor = 0
                for coord in coord_map:
                    try:
                        if (x + coord[0], y + coord[1]) in flashed and y + coord[1] >= 0 and x + coord[0] >= 0 and octopuses[y + coord[1]][x + coord[0]] > 9:
                            flashed_neighbor += 1
                    except IndexError: pass
                octopuses[y][x] += flashed_neighbor

    for octo in flashed:
        octopuses[octo[1]][octo[0]] = 0

    new_flashes = False
    for y, line in enumerate(octopuses):
        for x, octo in enumerate(line):
            if octo >= 10:
                new_flashes = True
                flashed.append((x, y))
                flashes += 1

    if show_octos == 2:
        print_octos(octopuses)

    if new_flashes: update(octopuses, flashed, show_octos=show_octos)

    nb_flashed = len(flashed)
    if nb_flashed > 0: return nb_flashed
    flashed.clear()

octopuses = copy.deepcopy(og_octopuses)
print("\033[3J")
step(octopuses, 100, show_octos = 0)    # 0: don't show; 1: show result of every step; 2: show every update
print(f"Part 1: {flashes}")
octopuses = copy.deepcopy(og_octopuses)
step(octopuses, 1, sync = True, show_octos = 1)
