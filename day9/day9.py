from time import sleep

with open("smaller_input.txt", "r") as f:
    data = f.read().strip().split('\n')

line_len = len(data[0])

def print_map(grid, to_print):
    height_map = "\033[1;32m" + (line_len * "- ") + '\n'

    for y_grid, line in enumerate(grid):
        for x_grid, height in enumerate(line):
            if ("low", x_grid, y_grid) in to_print:
                height_map += f"\033[1;36m{height} "
            elif height != '9':
                if (x_grid, y_grid) in all_water or (x_grid, y_grid, int(height)) in low_pts:
                    height_map += f"\033[1;0m{height} "
                else:
                    height_map += f"\033[1;35m{height} "
            else:
                height_map += f"\033[1;32m{height} "
        height_map += '\n'
    print(f"\r{height_map}")

low_pts = []
def part1(grid, show_map = False):
    global low_pts
    to_print = []
    risk_level = 0
    for y_grid, line in enumerate(grid):
        for x_grid, height in enumerate(line):
            left = x_grid ==  0 or line[x_grid - 1] > height
            right = x_grid == (line_len - 1) or line[x_grid + 1] > height
            up = y_grid == 0 or grid[y_grid - 1][x_grid] > height
            down = y_grid == (len(grid) - 1) or grid[y_grid + 1][x_grid] > height
            nb_lower = left + right + up + down

            if nb_lower == 4:
                if show_map: to_print.append(("low", x_grid, y_grid))
                risk_level += 1 + int(height)
                low_pts.append((x_grid, y_grid, int(height)))

    if show_map:
        print_map(grid, to_print)
        sleep(1)
    return risk_level

water = []
all_water = []
def basin(x_grid, y_grid, anim = False):
    global water, all_water
    grid = data[:]
    added = []

    if int(x_grid) != 0 and grid[y_grid][x_grid - 1] != '9' and (x_grid - 1, y_grid) not in water:
        added.append((x_grid - 1, y_grid))
    
    if int(x_grid) != line_len - 1 and grid[y_grid][x_grid + 1] != '9' and (x_grid + 1, y_grid) not in water:
        added.append((x_grid + 1, y_grid))

    if int(y_grid) != 0 and grid[y_grid - 1][x_grid] != '9' and (x_grid, y_grid - 1) not in water:
        added.append((x_grid, y_grid - 1))

    if int(y_grid) != len(data) - 1 and grid[y_grid + 1][x_grid] != '9' and (x_grid, y_grid + 1) not in water:
        added.append((x_grid, y_grid + 1))

    if len(added):
        water += added
        all_water += added
        if anim:
            print_map(data, low_pts)
            #sleep(0.1)
        for pt in added:
            basin(pt[0], pt[1])

def part2(anim = False):
    global low_pts
    
    if anim:
        print_map(data, low_pts)
        sleep(1)

    basin_sizes = []
    for pt in low_pts:              # (x, y, height)
        basin(pt[0], pt[1], anim = anim)
        #if anim: print_map(data, low_pts)
        basin_size = len(water)
        #print(f"pt: {pt}, size: {basin_size}")
        basin_sizes.append(basin_size)
        water.clear()
    basin_sizes.sort()

    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

print(f"\n\033[1;35mPart 1: \033[1;32m{part1(data, show_map = True)}\033[1;0m\n")
print(f"\n\033[1;35mPart 2: \033[1;32m{part2(anim = True)}\033[1;0m\n")
