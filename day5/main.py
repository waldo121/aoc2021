vents_map: [int] = [0] * 1000000
vents: [((int,int),(int,int))] = []
with open("./data", 'r') as file:
    [vents.append(
        ((int(c.split(' ')[0].split(',')[0]),int(c.split(' ')[0].split(',')[1])),
         (int(c.split(' ')[2].split(',')[0]),int(c.split(' ')[2].split(',')[1])))) for c in file]

# part 1
for vent in vents:
    x1 = vent[0][0]
    y1 = vent[0][1]
    x2 = vent[1][0]
    y2 = vent[1][1]
    if x1 == x2 and y1 != y2:
        if y1 > y2:
            for i in range(y2,y1 + 1):
                vents_map[i*1000 + x1] += 1
        else:
            for i in range(y1, y2 + 1):
                vents_map[i*1000 + x1] += 1

    if y1 == y2 and x1 != x2:
        if x1 > x2:
            for i in range(x2, x1 + 1):
                vents_map[y1*1000 + i] += 1
        else:
            for i in range(x1, x2 + 1):
                vents_map[y1*1000 + i] += 1
counter: int = 0
for cell in vents_map:
    if cell >= 2:
        counter += 1
print(counter)

# part 2
def generate_points(x1, y1, x2, y2) -> [(int,int)]:
    m: int = (y2-y1)//(x2-x1)
    b: int = y1 - x1 * m
    points: [(int,int)] = []
    # we now have y = mx+b
    if x1 > x2:
        for i in range(x2, x1 + 1):
            points.append((i, m * i + b))
    else:
        for i in range(x1, x2 + 1):
            points.append((i, m * i + b))
    return points

for vent in vents:
    x1 = vent[0][0]
    y1 = vent[0][1]
    x2 = vent[1][0]
    y2 = vent[1][1]
    if x1 != x2 and y1 != y2:
        diagonal_points = generate_points(x1,y1,x2,y2)
        for point in diagonal_points:
            vents_map[point[0] + point[1] * 1000] += 1
counter: int = 0
for cell in vents_map:
    if cell >= 2:
        counter += 1
print(counter)
