with open("input.txt", "r") as f:
    data = f.readlines()
    data = [_[:-1] for _ in data]
    lines = [_.split(" -> ") for _ in data]

points = [[] for list in lines]
for l_ind, line in enumerate(lines):
    for point in line:
        points[l_ind].append(point.split(","))

#print(points)

def get_max_coords(points):
    maxX = maxY = 0
    for line in points:
        for point in line:
            if int(point[0]) > maxX: maxX = int(point[0])
            if int(point[1]) > maxY: maxY = int(point[1])
    return (maxX, maxY)

max_coords = get_max_coords(points)


def solve(lines, diagonal = False, draw = False):
    coords = []
    for i in range((max_coords[0] + 1) * (max_coords[1] + 1)):
        coords.append(0)

    for line in points:
        if int(line[0][0]) == int(line[1][0]):
            startY = min(int(line[0][1]), int(line[1][1]))
            endY = max(int(line[0][1]), int(line[1][1])) + 1
            for p in range(startY, endY):
                coords[int(line[0][0]) + (p * (max_coords[0] + 1))] += 1
        elif int(line[0][1]) == int(line[1][1]):
            startX = min(int(line[0][0]), int(line[1][0]))
            endX = max(int(line[0][0]), int(line[1][0])) + 1
            for p in range(startX, endX):
                coords[p + (int(line[0][1]) * (max_coords[0] + 1))] += 1
        elif diagonal:
            if int(line[0][0]) < int(line[1][0]):
                x_increment = 1
            else: x_increment = -1
            if int(line[0][1]) < int(line[1][1]):
                y_increment = 1
            else: y_increment = -1
            for p in range(abs(int(line[0][0]) - int(line[1][0])) + 1):
                if p == 0:
                    coords[int(line[0][0]) + (int(line[0][1]) * (max_coords[0] + 1))] += 1
                elif p > 0:
                    coords[(int(line[0][0]) + (p * x_increment)) + ((int(line[0][1]) + (p * y_increment)) * (max_coords[0] + 1))] += 1
            
    overlaps = 0
    to_write = ""
    for index, coord in enumerate(coords):
        if coord >= 2: overlaps += 1
        if draw:
            if coord == 0: to_write += "."
            else: to_write += str(coord)
            if index % max_coords[0] == 0 and index != 0 and index < max_coords[0] + 1: to_write += "\n"
            elif (index + 1) % (max_coords[0] + 1) == 0: to_write += "\n"
    print(to_write, "\n")
    return overlaps

print(f"Part 1: {solve(points, draw = False)}")

print(f"Part 2: {solve(points, diagonal = True, draw = False)}")
