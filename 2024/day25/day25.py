from itertools import product

with open("input.txt", "r") as f:
    input = f.read()

schematics = input.split("\n\n")

keys: list[list[int]] = []
locks: list[list[int]] = []

for schematic in schematics:
    is_lock = True

    values = [0, 0, 0, 0, 0]

    for x, line in enumerate(schematic.splitlines()):
        if x == 0:
            is_lock = "#" in line
            continue

        for y, char in enumerate(line.strip()):
            if char == "#":
                values[y] = max(values[y], x if is_lock else 6 - x)

    locks.append(values) if is_lock else keys.append(values)


answer = 0

for key, lock in product(keys, locks):
    no_fit = False

    for key_value, lock_value in zip(key, lock):
        if key_value + lock_value > 5:
            no_fit = True

    if not no_fit:
        answer += 1

print(answer)
