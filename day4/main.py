import re
drawing_order: [int] = []
boards: [int] = []

with open("./data", 'r') as file:
    drawing_order = list(map(int, file.readline().rstrip().split(',')))
    lines = file.readlines()
    for index in range(len(lines)):
        if index % 6 == 0:
            continue
        boards += list(map(int, re.split('\s+',lines[index].rstrip().lstrip())))

def unmarked_score(drawn_number_map: [bool], start_index: int) -> int:
    score: int = 0
    consecutive_numbers: int = 0
    # check rows
    score = 0
    for i in range(5):
        consecutive_numbers = 0
        for j in range(5):
            if drawn_number_map[start_index + j + (i * 5)] == False:
                consecutive_numbers = 0
                break
            else:
                consecutive_numbers += 1
        if consecutive_numbers == 5:
            ## compute score
            for k in range(25):
                if drawn_number_map[start_index + k] == False:
                    score += boards[start_index + k]
            return score
    # check columns
    for i in range(5):
        consecutive_numbers = 0
        for j in range(5):
            if drawn_number_map[start_index + i + (j * 5)] == False:
                consecutive_numbers = 0
                break
            else:
                consecutive_numbers += 1
        if consecutive_numbers == 5:
            ## compute_score
            for k in range(25):
                if drawn_number_map[start_index + k] == False:
                    score += boards[start_index + k]
            return score
    return -1

def remove_board(boards: [int], exclude: int) -> [int]:
    if exclude in won_boards:
        boards.remove(exclude)
        return boards
    else:
        return boards
# Part 1
boards_number: int = len(boards) // 25
winning_score: int = -1
drawn_number_map: bool = [False] * len(boards)
for drawn_number in drawing_order:
    drawn_number_indexes = [index for index in range(len(boards)) if boards[index] == drawn_number]
    for index in drawn_number_indexes:
        drawn_number_map[index] = True
    for board_index in range(boards_number):
        tmp_score = unmarked_score(drawn_number_map, board_index * 25)
        if tmp_score != -1:
            winning_score = tmp_score * drawn_number
            break
    if winning_score != -1:
        break
print(winning_score)
# Part 2
unwon_boards: [int] = [i for i in range(boards_number)]
drawn_number_map = [False] * len(boards)
winning_score = -1
for drawn_number in drawing_order:
    drawn_number_indexes = [index for index in range(len(boards)) if boards[index] == drawn_number]
    for index in drawn_number_indexes:
        drawn_number_map[index] = True
    for board_index in range(boards_number):
        tmp_score = unmarked_score(drawn_number_map, board_index * 25)
        if tmp_score != -1:
            unwon_boards = remove_board(unwon_boards, board_index)
            if len(unwon_boards) == 0:
                winning_score = tmp_score * drawn_number
                break
    if winning_score != -1:
        break
print(winning_score)
