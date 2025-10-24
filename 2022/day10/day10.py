with open("input.txt") as f:
    instructions = f.read().splitlines()


cycles = []
for instruction in instructions:
    if instruction == "noop":
        cycles.append(0)
    else:
        cycles.append(0)
        cycles.append(int(instruction[5:]))


sprite = []
x = 1
total = 0
for i in range(1, 241):
    if abs(x - ((i - 1) % 40)) > 1:
        sprite.append("  ")
    else:
        sprite.append("██")

    if i in [20, 60, 100, 140, 180, 220]:
        total += x * i

    x += cycles[i - 1]


print(total)

for x, char in enumerate(sprite):
    print(char, end="\n" if (x + 1) % 40 == 0 else "")
