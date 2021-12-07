from statistics import median

with open("input.txt", "r") as f:
    data = [int(pos) for pos in f.read().strip().split(",")]

def fuel_usage(pos, part):
    fuel = 0
    if part == 1:
        for original_pos in data:
            fuel += abs(original_pos - pos)
    elif part == 2:
        for original_pos in data:
            n = abs(original_pos - pos)
            fuel += ((n**2) + n) / 2
    return (fuel, pos)

def solve(part):
    furthest = max(data)
    positions = [pos for pos in range(furthest + 1)] 
    min_fuel = min([fuel_usage(pos, part) if part == 2 else fuel_usage(int(median(data)), 1) for pos in positions])
    return min_fuel

part1 = solve(1)
print(f"Part 1:\n\tCheapest position: {part1[1]}\n\tFuel usage: {part1[0]}")
part2 = solve(2)
print(f"Part 2:\n\tCheapest position: {part2[1]}\n\tFuel usage: {int(part2[0])}")
