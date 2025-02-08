from collections import defaultdict
from heapq import heappop, heappush
from typing import Iterator

Position = tuple[int, int]
State = tuple[int, Position]
Maze = list[str]


def load_maze() -> Maze:
    with open("input.txt", "r") as file:
        maze: Maze = file.readlines()

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


def get_options(current_state: State, maze: Maze) -> Iterator[tuple[int, State]]:
    current_rotation, current_direction = current_state

    yield 1000, ((current_rotation - 1) % 4, current_direction)
    yield 1000, ((current_rotation + 1) % 4, current_direction)

    directions: list[Position] = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    current_row, current_col = current_direction
    direction_row, direction_col = directions[current_rotation]
    offsetted = current_row + direction_row, current_col + direction_col
    offsetted_row, offsetted_col = offsetted

    if maze[offsetted_row][offsetted_col] != "#":
        yield 1, (current_rotation, offsetted)


def find_shortest_paths(
    maze: Maze, start: Position, end: Position
) -> Iterator[list[State]]:
    dist: defaultdict[State, float] = defaultdict(lambda: float("inf"))
    prev: defaultdict[State, list[State]] = defaultdict(list)

    queue: list[tuple[int, State]] = []
    heappush(queue, (0, (0, start)))

    while queue:
        current_dist, current_state = heappop(queue)

        if current_state[1] == end:
            break

        for option_dist, option in get_options(current_state, maze):
            next_dist = current_dist + option_dist

            if next_dist < dist[option]:
                dist[option] = next_dist
                heappush(queue, (next_dist, option))
                prev[option] = [current_state]
            elif next_dist == dist[option]:
                prev[option].append(current_state)
    else:
        raise RuntimeError("No path found")

    def walk(state: State) -> Iterator[list[State]]:
        if state[1] == start:
            yield [state]
            return

        for previous_state in prev[state]:
            for path in walk(previous_state):
                yield path + [state]

    return walk(current_state)


maze = load_maze()
start, end = find_start_end(maze)
shortest_paths = find_shortest_paths(maze, start, end)
answer = len({position for path in shortest_paths for _, position in path})
print(answer)
