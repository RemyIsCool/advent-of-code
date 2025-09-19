from __future__ import annotations

from collections import defaultdict
from itertools import permutations

with open("input.txt", "r") as f:
    connections_list = f.readlines()


distances: defaultdict[tuple[str, str], int] = defaultdict(lambda: 10**100)
all_places: set[str] = set()

for line in connections_list:
    places, distance = line.split(" = ")
    from_place, to_place = places.split(" to ")
    distance = int(distance)
    all_places.add(from_place)
    all_places.add(to_place)

    if distances[(from_place, to_place)] > distance:
        distances[(from_place, to_place)] = distance
    if distances[(to_place, from_place)] > distance:
        distances[(to_place, from_place)] = distance

options: list[int] = []

for option in list(permutations(all_places)):
    length = 0
    for place_a, place_b in zip(option, option[1:]):
        length += distances[(place_a, place_b)]
    options.append(length)

print(min(options))
print(max(options))
