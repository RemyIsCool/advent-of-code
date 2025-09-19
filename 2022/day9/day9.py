with open("input.txt") as f:
    puzzle_input = f.readlines()

knots = [(0, 0) for _ in range(10)]

positions = {(0, 0)}

for line in puzzle_input:
    parts = line.split()
    direction = parts[0]
    distance = int(parts[1])

    (dx, dy) = {"R": (1, 0), "L": (-1, 0), "D": (0, 1), "U": (0, -1)}[direction]

    for _ in range(distance):
        knots[0] = (knots[0][0] + dx, knots[0][1] + dy)

        for i in range(1, len(knots)):
            dist_x = knots[i - 1][0] - knots[i][0]
            dist_y = knots[i - 1][1] - knots[i][1]

            if abs(dist_x) > 1 or abs(dist_y) > 1:
                if dist_x != 0 and dist_y != 0:
                    if dist_x > 0 and dist_y > 0:
                        knots[i] = (knots[i][0] + 1, knots[i][1] + 1)
                    elif dist_x > 0 and dist_y < 0:
                        knots[i] = (knots[i][0] + 1, knots[i][1] - 1)
                    elif dist_x < 0 and dist_y > 0:
                        knots[i] = (knots[i][0] - 1, knots[i][1] + 1)
                    else:
                        knots[i] = (knots[i][0] - 1, knots[i][1] - 1)
                else:
                    if dist_x > 0:
                        knots[i] = (knots[i][0] + 1, knots[i][1])
                    if dist_x < 0:
                        knots[i] = (knots[i][0] - 1, knots[i][1])
                    if dist_y > 0:
                        knots[i] = (knots[i][0], knots[i][1] + 1)
                    if dist_y < 0:
                        knots[i] = (knots[i][0], knots[i][1] - 1)

        positions.add(knots[-1])

print(len(positions))
