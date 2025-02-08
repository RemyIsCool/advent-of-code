with open("day6/input.txt", "r") as f:
    input = f.read()


def calculate(count):
    for x in range(len(input)):
        sliced = input[x : x + count]
        if len(set(sliced)) == count:
            return x + count


print(calculate(4), calculate(14))
