from copy import deepcopy


with open("input.txt", "r") as f:
    initial_state = f.readlines()


state = []
for line in initial_state:
    line = line.strip()
    row = []
    for char in line:
        row.append(char == "#")
    state.append(row)
print(state)

rows = len(state)
cols = len(state[0])


def print_state(state):
    for row in state:
        for cell in row:
            print("#" if cell else ".", end="")
        print()
    print()


for _ in range(100):
    next_state = deepcopy(state)

    for row, cells in enumerate(state):
        for col, cell in enumerate(cells):
            neighbor_count = 0
            for dr, dc in (
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, 1),
                (1, 0),
                (1, -1),
            ):
                if row + dr >= rows or col + dc >= cols or row + dr < 0 or col + dc < 0:
                    neighbor = False
                else:
                    neighbor = state[row + dr][col + dc]
                neighbor_count += int(neighbor)

            current = state[row][col]

            if neighbor_count > 3 or neighbor_count < 2:
                next_state[row][col] = False
            if neighbor_count == 3:
                next_state[row][col] = True

            if (row, col) in [
                (0, 0),
                (0, cols - 1),
                (rows - 1, 0),
                (rows - 1, cols - 1),
            ]:
                next_state[row][col] = True

    print_state(next_state)
    state = deepcopy(next_state)

ans = 0
for row in state:
    for cell in row:
        ans += int(cell)

print(ans)
