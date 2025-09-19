with open("input.txt", "r") as f:
    input = f.readlines()

grid = [[0 for _ in range(1000)] for _ in range(1000)]

for line in input:
    tokens = line.split()
    command = tokens[0]
    if command == "turn":
        command = tokens[1]
        tokens.pop(0)
    tokens.pop(0)
    start, _, end = tokens
    (start_x, start_y), (end_x, end_y) = start.split(","), end.split(",")
    start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(end_x), int(end_y)

    match command:
        case "off":
            for y, row in enumerate(grid[start_y : end_y + 1], start=start_y):
                for x, col in enumerate(row[start_x : end_x + 1], start=start_x):
                    grid[y][x] -= 1
                    if grid[y][x] < 0:
                        grid[y][x] = 0

        case "on":
            for y, row in enumerate(grid[start_y : end_y + 1], start=start_y):
                for x, col in enumerate(row[start_x : end_x + 1], start=start_x):
                    grid[y][x] += 1

        case "toggle":
            for y, row in enumerate(grid[start_y : end_y + 1], start=start_y):
                for x, col in enumerate(row[start_x : end_x + 1], start=start_x):
                    grid[y][x] += 2

ans = 0
for row in grid:
    for item in row:
        ans += item

print(ans)
