from collections import defaultdict


with open("day5/input.txt", "r") as f:
    input = f.read()

boxes, instructions = input.split("\n\n")

columns = [list() for _ in range(int(boxes[-1][-1]) + 1)]

for line in boxes.splitlines()[:-1]:
    for x, char in enumerate(line[1::4]):
        if not char.isspace():
            columns[x].append(char)

for instruction in instructions.splitlines():
    count, from_stack, to_stack = map(int, instruction.split(" ")[1::2])

    columns[to_stack - 1] = columns[from_stack - 1][:count] + columns[to_stack - 1]
    columns[from_stack - 1] = columns[from_stack - 1][count:]

print("".join([c[0] for c in columns if c]))
