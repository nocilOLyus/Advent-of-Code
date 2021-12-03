with open("input.txt", "r") as f:
    binarynb = [line.strip() for line in f.readlines()]
    ones = zeros = 0
    gamma = epsilon = ""

    def most_common_bit(numbers, pos):
        "Returns (most common, least common)"

        zeros = ones = 0
        for number in numbers:
            if number[pos] == '0': zeros += 1
            if number[pos] == '1': ones += 1
        if zeros > ones:
            return ('0', '1')
        elif ones >= zeros:
            return ('1', '0')
    
    # Part 1

    for i in range(len(binarynb[0])):
        bit_tuple = most_common_bit(binarynb, i)
        gamma += bit_tuple[0]
        epsilon += bit_tuple[1]
    
    gamma_dec = int(gamma, 2)
    epsilon_dec = int(epsilon, 2)

    print(gamma_dec, epsilon_dec)
    print(gamma_dec * epsilon_dec)


    # Part 2

    bit_tuple = most_common_bit(binarynb, 0)
    oxygen_rating = [number for number in binarynb if number[0] == bit_tuple[0]]
    co2_rating = [number for number in binarynb if number[0] == bit_tuple[1]]

    i = 1
    while len(oxygen_rating) > 1:
        bit_tuple = most_common_bit(oxygen_rating, i)
        o_rat = oxygen_rating[:]
        for number in o_rat:
            if number[i] != bit_tuple[0]: oxygen_rating.remove(number)
        i += 1

    i = 1
    while len(co2_rating) > 1:
        bit_tuple = most_common_bit(co2_rating, i)
        c_rat = co2_rating[:]
        for number in c_rat:
            if number[i] != bit_tuple[1]: co2_rating.remove(number)
        i += 1

    print(oxygen_rating)
    print(co2_rating)
    oxygen_rating = int(oxygen_rating[0], 2)
    co2_rating = int(co2_rating[0], 2)

    print(oxygen_rating, co2_rating)
    print(oxygen_rating * co2_rating)
