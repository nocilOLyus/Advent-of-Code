with open("input.txt", "r") as f:
    data = [line.split(" | ") for line in f.read().strip().split("\n")]

signals = [d[0].split(" ") for d in data]
for display in signals:
    display.sort(key=len)
val = [d[1].split(" ") for d in data]

out_val = []
for i in range(len(val)):
    out_val += val[i]

unique_lengths = [2, 4, 3, 7]

numbers = ["abcdef", "bc", "abdeg", "abcdg", "bcfg", "acdfg", "acdefg", "abc", "abcdefg", "abcdfg"]

numbers_translated = []

def solve1(values):
    sol = 0
    for val in values:
        if len(val) in unique_lengths:
            sol += 1
    return sol

def decode(index, letters):
    order = "abcdefg"
    number = ""
    for seg in val[index]:
        segments = ""
        for letter in seg:
            segments += order[letters.index(letter)]
        segments = ''.join(sorted(segments))
        number += str(numbers.index(segments))
    numbers_translated.append(int(number))

def solve2(signals):
    # Indexes/Numbers: 0/1 | 1/7 | 2/4 | 9/8

    for index, display in enumerate(signals):
        a = b = c = d = e = f = g = ''              # following BCD/7seg convention

        common_7 = set(display[0]) & set(display[1])
        for l in display[1]:
            if l not in common_7: a = l                                     # a

        for nb in display:
            common_4 = set(display[2]) & set(nb)
            common_7 = set(display[1]) & set(nb)

            if len(nb) == 6:
                if not len(d) and len(common_4) == 4:
                    for l in nb:
                        if l not in display[2] and l != a: d = l            # d

                elif not len(g) and len(common_7) == 3:
                    for l in display[-1]:
                        if l not in nb: g = l                               # g

                elif not len(b) and len(common_7) == 2:
                    for l in display[-1]:
                        if l not in nb: b = l                               # b

            elif len(nb) == 5:
                if len(common_7) == 3:
                    common_3_4 = set(display[2]) & set(nb)

                    if not len(e):
                        for l in display[-1]:
                            if l not in nb and l not in display[2]: e = l   # e

                    if not len(f):
                        for l in display[2]:
                            if l not in nb: f = l                           # f

                elif len(common_7) == 2 and len(common_4) == 2:
                        for l in display[0]:
                            if l not in nb: c = l                           # c

        letters = a + b + c + d + e + f + g
        decode(index, letters)
    return sum(numbers_translated)
        
print(f"Part 1: {solve1(out_val)}")
print(f"Part 2: {solve2(signals)}")
