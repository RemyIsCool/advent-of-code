with open("input.txt") as f:
    lines = f.readlines()

keys = {
    (2, 0): "1",
    (1, 1): "2",
    (2, 1): "3",
    (3, 1): "4",
    (0, 2): "5",
    (1, 2): "6",
    (2, 2): "7",
    (3, 2): "8",
    (4, 2): "9",
    (1, 3): "A",
    (2, 3): "B",
    (3, 3): "C",
    (2, 4): "D",
}

pos = (1, 1)

code = []

for line in lines:
    for char in line.strip():
        x, y = pos
        new = {"U": (x, y - 1), "D": (x, y + 1), "L": (x - 1, y), "R": (x + 1, y)}[char]
        if new in keys:
            pos = new

    code.append(keys[pos])

print("".join(code))
