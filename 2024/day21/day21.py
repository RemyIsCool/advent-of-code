from functools import cache
from itertools import product

NUMERIC = "789456123 0A"
DIRECTIONAL = " ^A<v>"


@cache
def paths(keymap: str) -> dict[tuple[str, str], list[str]]:
    locations = {
        c: (x, y)
        for y, row in enumerate(keymap[i : i + 3] for i in range(0, len(keymap), 3))
        for x, c in enumerate(row)
    }

    pathmap = {}

    for a, b in product((c for c in keymap if c != " "), repeat=2):

        # same cell, no moves necessary
        if a == b:
            pathmap[a, b] = [""]
            continue

        (ax, ay), (bx, by) = locations[a], locations[b]
        dx, dy = bx - ax, by - ay

        # always move in a straight line
        moves_x = [">", "<"][dx < 0] * abs(dx)
        moves_y = ["v", "^"][dy < 0] * abs(dy)

        # only moving Y-axis
        if dx == 0:
            pathmap[a, b] = [moves_y]

        # only moving X-axis
        elif dy == 0:
            pathmap[a, b] = [moves_x]

        # X-axis move hits the gap, move Y-axis first
        elif locations[" "] == (bx, ay):
            pathmap[a, b] = [moves_y + moves_x]

        # Y-axis move hits the gap, move X-axis first
        elif locations[" "] == (ax, by):
            pathmap[a, b] = [moves_x + moves_y]

        # either path avoids the gap
        else:
            pathmap[a, b] = [moves_x + moves_y, moves_y + moves_x]

    return pathmap


@cache
def presses(code: str, depth: int, keypad: str = NUMERIC) -> int:
    if depth == 1:
        return len(code)

    keypaths = paths(keypad)
    return sum(
        min(presses(path + "A", depth - 1, DIRECTIONAL) for path in keypaths[pair])
        for pair in zip("A" + code, code)
    )


with open("input.txt") as f:
    codes = [line.strip() for line in f.readlines()]

for robots in (2, 25):
    complexity = sum(presses(code, robots + 2) * int(code[:-1]) for code in codes)
    print(f"Total complexity ({robots} robots): {complexity}")
