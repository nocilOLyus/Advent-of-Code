from collections import deque           # to rotate list
from time import sleep

with open("input.txt", "r") as f:
    state_str = f.read().split(",")
    state = [int(fish) for fish in state_str]

nb_fish = deque([])
for i in range(9):
    nb_fish.append(0)
    nb_fish[i] = state.count(i)

def update(school, day = 1):
    global nb_fish
    while day >= 1:
        nb_fish.rotate(-1)
        nb_fish[6] += nb_fish[8]
        day -= 1

def solve(school):
    total = 0
    for cell in school:
        total += cell
    return total

update(nb_fish, 256)
#print(nb_fish)
print(f"Number of fish: {solve(nb_fish)}")
