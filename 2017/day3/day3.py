from collections import defaultdict

puzzle_input = int(input())

x, y = 0, 0

count = 0
length = 1
increase = False
direction = 0

values = defaultdict(int)
values[(0, 0)] = 1

max_value = 0
while max_value < puzzle_input:
    x, y = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)][direction]

    res = sum(values[(x + i, y + j)] for i in range(-1, 2) for j in range(-1, 2))
    max_value = max(max_value, res)
    values[(x, y)] = res

    count += 1
    if count >= length:
        if increase:
            length += 1
        direction += 1
        direction %= 4
        increase = not increase
        count = 0

print(max_value)
