data: [(str, int)] = []

with open("./data", 'r') as file:
    [data.append((c.split(' ')[0], int(c.split(' ')[1].rstrip()))) for c in file]


# Part 1
h_pos: int = 0
v_pos: int = 0
for instruction in data:
    if instruction[0] == 'forward':
        h_pos += instruction[1]
    elif instruction[0] == 'down':
        v_pos += instruction[1]
    else:
        v_pos -= instruction[1]
print(h_pos*v_pos)

# Part 2
h_pos: int = 0
v_pos: int = 0
aim: int = 0
for instruction in data:
    if instruction[0] == 'forward':
        h_pos += instruction[1]
        v_pos += aim * instruction[1]
    elif instruction[0] == 'down':
        aim += instruction[1]
    else:
        aim -= instruction[1]
print(h_pos*v_pos)
