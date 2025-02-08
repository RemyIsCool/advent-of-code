from string import ascii_letters

with open("day3/input.txt", "r") as f:
    input = [l.strip() for l in f.readlines()]

a = 0
for x in range(0, len(input), 3):
    both = set(input[x]) & set(input[x + 1]) & set(input[x + 2])
    both = list(both)[0]
    a += ascii_letters.index(both) + 1

print(a)
