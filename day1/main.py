data: [int] = []

with open("./data", 'r') as file:
    [data.append(int(c.rstrip())) for c in file]

# Part 1
current: int = -1
previous: int = -1
increase_counter: int = 0

for d in data:
    if current != -1:
        previous = current
    current = d
    if previous != -1:
        if current > previous:
            increase_counter += 1
print(increase_counter)

increase_counter = 0

# Part 2
increase_counter = 0
current_sum: int = -1
previous_sum: int = -1
for i in range(len(data)-2):
    if current_sum != -1:
        previous_sum = current_sum
    current_sum = data[i] + data[i+1] + data[i+2]
    if previous_sum != -1:
        if current_sum > previous_sum:
            increase_counter += 1
print(increase_counter)
