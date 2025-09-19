from tqdm import tqdm


with open("input.txt", "r") as f:
    target = int(f.read())


houses = [0 for _ in range(target)]

for elf in tqdm(range(1, target)):
    c = 0
    for house in range(elf, target, elf):
        houses[house] += elf * 11
        c += 1

        if c > 50:
            break

for x, house in enumerate(houses):
    if house >= target:
        print(x)
        break
