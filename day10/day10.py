with open("input.txt", "r") as f:
    data = f.read().strip().split('\n')

syntax = {'(': ')', '[': ']', '{': '}', '<': '>'}
error_pts = {')': 3, ']': 57, '}': 1197, '>': 25137}
autocomp_pts = {')': 1, ']': 2, '}': 3, '>': 4}
incomplete = []

def syntax_err_score(line):
    stack = []
    for char in line:
        if char in syntax.keys(): stack.append(char)
        else:
            last = stack.pop()
            if syntax[last] != char: return error_pts[char]            

def complete_line(line):
    stack = []
    rest = ""
    for char in line:
        if char in syntax.keys(): rest = syntax[char] + rest
        else: rest = rest[1:]
    return rest

def autocomp_score(rest):
    score = 0
    for char in rest:
        score *= 5
        score += autocomp_pts[char]
    return score

def part1():
    scores = []
    for line in data:
        score = syntax_err_score(line)
        if score != None: scores.append(score)
        else: incomplete.append(line)
    
    print(f"Part 1: {sum(scores)}")

def part2():
    scores = []
    for line in incomplete:
        scores.append(autocomp_score(complete_line(line)))

    scores.sort()

    print(f"Part 2: {scores[int((len(scores) - 1) / 2)]}")


part1()
part2()