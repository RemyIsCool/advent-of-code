with open("input.txt", "r") as f:
    input = f.read()

input = input.strip().splitlines()

x, y, a = 0, 0, 0
for line in input:
    dir, len = line.split()
    len = int(len)

    match dir:
        case "down":
            a += len
        case "up":
            a -= len
        case "forward":
            x += len
            y += a * len

print(x * y)
