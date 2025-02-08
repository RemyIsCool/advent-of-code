with open("input.txt", "r") as file:
    input_lines: list[str] = file.readlines()

wires: list[list[str]] = [line.split(",") for line in input_lines]

all_points: list[list[tuple[int, int]]] = []

for wire in wires:
    position: tuple[int, int] = (0, 0)

    all_points.append([])

    for command in wire:
        direction: str = command[0]
        distance: int = int(command[1:])

        for x in range(distance):
            position = {
                "U": (position[0], position[1] - 1),
                "D": (position[0], position[1] + 1),
                "R": (position[0] + 1, position[1]),
                "L": (position[0] - 1, position[1]),
            }[direction]

            all_points[-1].append(position)

v = min(
    set(all_points[0]) & set(all_points[1]),
    key=lambda x: all_points[0].index(x) + all_points[1].index(x),
)
print(all_points[0].index(v) + all_points[1].index(v) + 2)
