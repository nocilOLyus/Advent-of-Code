with open("input.txt", "r") as f:
    movements = f.read().split('\n')
    movements.remove('')

    depth = 0
    distance = 0
    aim = 0 

    for move in movements:
        if move[:-2] == "forward":
            distance += int(move[-1])
            depth += aim * int(move[-1])
        elif move[:-2] == "up":
            aim -= int(move[-1])
        elif move[:-2] == "down":
            aim += int(move[-1])

    print(depth, distance)
    print(depth * distance)
