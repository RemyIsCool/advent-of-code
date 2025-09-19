puzzle_input = int(input())
puzzle_input = 50


ring = 8
ring_count = 0

x, y = 1, 0
dx, dy = 0, -1

movement_counter = 0

for x in range(2, puzzle_input):
    ring_count += 1
    movement_counter += 1
    if movement_counter > ring_count / 4:
        movement_counter = 0

        if dx == 0 and dy == 1:
            dx = -1
            dy = 0
        elif dx == 0 and dy == -1:
            dx = 1
            dy = 0
        elif dx == 1 and dy == 0:
            dx = 0
            dy = 1
        else:
            dx = 0
            dy = -1
    x += dx
    y += dy
    print(x, y)
    if ring_count > ring:
        ring += 8
        ring_count = 0
