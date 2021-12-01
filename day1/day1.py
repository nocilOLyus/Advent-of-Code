with open("input.txt", "r") as f:
    measurements = f.read()
    measurements = measurements.split('\n')
    measurements.remove('')

    previous_depth = int(measurements[0])
    increased = 0
    sums = []
    sum_increased = 0

    # Part 1
    for depth in measurements:
        if int(depth) > previous_depth:
            increased += 1
        previous_depth = int(depth)

    # Part 2
    for start in range(len(measurements) - 2):
        sum = int(measurements[start]) + int(measurements[start + 1]) + int(measurements[start + 2])
        sums.append(sum)
        if len(sums) == 2:
            if sums[1] > sums[0]:
                sum_increased += 1
            sums[0] = sums[1]
            sums.pop()

    print(increased)
    print(sum_increased)
