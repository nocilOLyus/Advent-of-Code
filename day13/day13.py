from copy import deepcopy

with open("input.txt", "r") as f:
    data = [coord for coord in f.read().strip().split('\n')]

coords = [tuple(map(int, coords)) for coords in [coord.split(',') for coord in data[:data.index('')]]]
instructions = [instruction[2].split('=') for instruction in [instruction.split(' ') for instruction in data[data.index('') + 1:]]]

foldY = [int(instruction[1]) for instruction in instructions if instruction[0] == 'y']
foldX = [int(instruction[1]) for instruction in instructions if instruction[0] == 'x']

#print("coords", coords)
#print("instructions:", instructions)



def visualize(paper):
    maxX = maxY = 0
    for coord in paper:
        if coord[0] > maxX: maxX = coord[0]
        if coord[1] > maxY: maxY = coord[1]

    for y in range(maxY + 1):
        for x in range(maxX + 1):
            if x in foldX and y in foldY: print("|", end="")
            elif x not in foldX and y in foldY: print("-", end="")
            elif x in foldX and y not in foldY: print("|", end="")
            elif x not in foldX and y not in foldY:
                if (x, y) in paper: print("#", end=" ")
                else: print(" ", end=" ")
        print()
    print()

def fold(paper, fold):
    foldX = foldY = 0
    if fold[0] == 'x': foldX = int(fold[1])
    elif fold[0] == 'y': foldY = int(fold[1])

    if foldY > 0:
        top = [coord for coord in paper if coord[1] <= foldY]
        bottom = [coord for coord in paper if coord[1] > foldY]
        paper = deepcopy(top)
        
        for coord in bottom:
            if coord not in paper: paper.append((coord[0], foldY - (coord[1] - foldY)))
        return paper

    elif foldX > 0:
        left = [coord for coord in paper if coord[0] <= foldX]
        right = [coord for coord in paper if coord[0] > foldX]
        paper = deepcopy(left)

        for coord in right:
            if coord not in paper: paper.append((foldX - (coord[0] - foldX), coord[1]))
        return paper

def solve(coords, instructions, folds = len(instructions), visual = False, visual_end = False):
    paper = deepcopy(coords)
    instruc = deepcopy(instructions)

    if visual: visualize(paper)

    while folds == -1 or folds > 0:
        f = instruc[0]
        del instruc[0]
        paper = fold(paper, f)
        if visual: visualize(paper)
        folds -= 1
        
    if visual_end: visualize(paper)
    return len(set(paper))

print(f"Part 1: {solve(coords, instructions, folds = 1)} dots visible.\n")
print(f"Part 2: {solve(coords, instructions, visual_end = True)} dots visible.")