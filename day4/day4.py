with open("input.txt", "r") as f:
    all = f.readlines()
    numbers_to_draw = all[0].split(',')
    boards = [[]]
    i = 0
    for line in range(2, len(all)):
        if all[line] != '\n':
            boards[i] += all[line].split(' ')
        else:
            boards.append([])
            i += 1

for index, number in enumerate(numbers_to_draw):
    if number[-1] == '\n':
        numbers_to_draw[index] = number[:-1]

marked_boards = []
def reset_marked_boards(_ = marked_boards):
    marked_boards.clear()
    for board in boards:
        while '' in board:
            board.remove('')
        for index, number in enumerate(board):
            if number[-1] == '\n':
                board[index] = number[:-1]
        marked_boards.append([])

bingo = []
def check_bingo(board):
    if board not in bingo:
        mult5_count = 1
        consecutive = 1
        current_board = marked_boards[board]
        #nd its middle print(f"Marked: {current_board}")
        for index, number in enumerate(current_board):
            if index + 1 < len(current_board) and number + 1 in current_board and (number + 1) % 5 != 0: consecutive += 1
            else: consecutive = 1
            for i in range(1, 5):
                if number + (i * 5) in current_board:
                    mult5_count += 1
                else: break
            #print(f"consecutive: {consecutive}\nmult5: {mult5_count}")
            if consecutive == 5 or mult5_count == 5:
                bingo.append(board)
                return True
            elif mult5_count < 5: mult5_count = 1
    elif board in bingo: return False

def mark(number, board):
    if number in boards[board]:
        index_num = boards[board].index(str(number))
        marked_boards[board].append(index_num)
        marked_boards[board].sort()

last_bingo_board = []
def fill_boards(win = True):
    for number in numbers_to_draw:
        for board in range(len(boards)):
            mark(number, board)
            #print(f"{number} marked on board {board}")
            if check_bingo(board):
                if win:
                    #print(f"board: {boards[board]}\nmarked board: {marked_boards[board]}\nBINGO !")
                    return (board, number)
                elif not win:
                    last_bingo = (board, number)
                    last_bingo_board = marked_boards[board][:]
    return [last_bingo, last_bingo_board]

def sum_unmarked(board):
    sum = 0
    for i in range(25):
        if i not in marked_boards[board]:
            sum += int(boards[board][i])
    return sum


def part1():
    reset_marked_boards()
    answer = fill_boards()
    winning_board = answer[0]
    last_number = int(answer[1])
    sum_u = sum_unmarked(winning_board)
    score = sum_u * last_number
    #print(f"Winning board: {winning_board}\nLast number: {last_number}\nSum: {sum_u}")
    print(f"Part 1: {score}")

part1()


def part2():
    reset_marked_boards()
    result = fill_boards(win = False)
    last_bingo = result[0]
    losing_board = last_bingo[0]
    last_number = int(last_bingo[1])
    last_bingo_board = result[1]
    marked_boards[losing_board] = last_bingo_board
    sum_u = sum_unmarked(losing_board)
    score = sum_u * last_number
    print(f"Part 2: {score}")

part2()
