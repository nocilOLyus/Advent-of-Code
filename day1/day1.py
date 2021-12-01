with open("input.txt", "r") as f:
    measurements = f.read().split('\n')
    measurements.remove('')

    previous_depth = int(measurements[0])
    increased = 0
    sums = []

    # Part 1
    for depth in measurements:
        if int(depth) > previous_depth:
            increased += 1
        previous_depth = int(depth)
    print(increased)

    # Part 2
    increased = 0
    for start in range(len(measurements) - 2):
        sum = int(measurements[start]) + int(measurements[start + 1]) + int(measurements[start + 2])
        sums.append(sum)
        if len(sums) == 2:
            if sums[1] > sums[0]:
                increased += 1
            sums[0] = sums[1]
            sums.pop()

    print(increased)
