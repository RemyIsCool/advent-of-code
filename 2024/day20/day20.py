from collections import defaultdict
from typing import Iterator

Position = tuple[int, int]
State = tuple[bool, Position]
Maze = list[str]


def load_maze() -> Maze:
    with open("input.txt", "r") as file:
        input = file.read()

    maze: Maze = list(input.splitlines())
    return maze


def find_start_end(maze: Maze) -> tuple[Position, Position]:
    start: Position = (0, 0)
    end: Position = (0, 0)

    for row, line in enumerate(maze):
        for col, char in enumerate(line):
            position: Position = (row, col)

            if char == "S":
                start = position

            if char == "E":
                end = position

    return start, end


def get_neighbors(position: Position, maze: Maze) -> Iterator[Position]:
    position_row, position_col = position

    for direction_row, direction_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        offsetted = (
            position_row + direction_row,
            position_col + direction_col,
        )
        offsetted_row, offsetted_col = offsetted

        if (
            offsetted_row >= len(maze)
            or offsetted_row < 0
            or offsetted_col >= len(maze)
            or offsetted_col < 0
            or maze[offsetted_row][offsetted_col] == "#"
        ):
            continue

        yield offsetted


def find_distances(maze: Maze, end: Position) -> defaultdict[Position, float]:
    queue: list[Position] = [end]
    dist: defaultdict[Position, float] = defaultdict(lambda: float("inf"))
    dist[end] = 0

    while queue:
        current = queue.pop(0)

        for neighbor in get_neighbors(current, maze):
            if neighbor in dist:
                continue

            dist[neighbor] = dist[current] + 1
            queue.append(neighbor)

    return dist


def get_cheats(
    distances: dict[Position, float], available_cheats: set[Position]
) -> int:
    count = 0

    for position, distance in distances.items():
        position_row, position_col = position

        for direction_row, direction_col in available_cheats:
            offsetted = position_row + direction_row, position_col + direction_col

            if offsetted not in distances:
                continue

            savings = (
                distance
                - distances[offsetted]
                - (abs(direction_row) + abs(direction_col))
            )

            if savings >= 100:
                count += 1

    return count


def gen_available_cheats(distance: int) -> set[Position]:
    cheats: set[Position] = {(0, 0)}

    for _ in range(distance):
        cheats_copy = cheats.copy()

        for cheat_row, cheat_col in cheats_copy:
            for direction_row, direction_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                offsetted = cheat_row + direction_row, cheat_col + direction_col

                cheats.add(offsetted)

    return cheats


maze = load_maze()
start, end = find_start_end(maze)
distances = find_distances(maze, end)

cheats_1 = gen_available_cheats(2)
print("Part 1:", get_cheats(dict(distances), cheats_1))

cheats_2 = gen_available_cheats(20)
print("Part 2:", get_cheats(dict(distances), cheats_2))
