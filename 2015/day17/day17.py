from itertools import combinations


with open("input.txt", "r") as f:
    container_sizes = [int(s) for s in f.readlines()]


counter = 0

for x in range(1, len(container_sizes) + 1):
    is_min = False
    for combo in combinations(container_sizes, x):
        if sum(combo) == 150:
            counter += 1
            is_min = True
    if is_min:
        break


print(counter)
