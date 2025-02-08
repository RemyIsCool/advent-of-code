with open("input.txt", "r") as file:
    input = file.readlines()

n = 0
visited = [0]

# expect it to take ~30s
while True:
    stop = False
    for line in input:
        op, num = line[0], int(line[1:])
        match op:
            case "+":
                n += num
            case "-":
                n -= num

        if n in visited:
            print(n)
            stop = True
            break
        visited.append(n)
    if stop:
        break
