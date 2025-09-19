with open("input.txt", "r") as f:
    ingredients = f.readlines()

scores: list[tuple[int, int, int, int, int]] = []

for line in ingredients:
    words = line.split()
    capacity = int(words[2][:-1])
    durability = int(words[4][:-1])
    flavor = int(words[6][:-1])
    texture = int(words[8][:-1])
    calories = int(words[-1])
    scores.append((capacity, durability, flavor, texture, calories))

combos: list[int] = []

for a in range(100):
    for b in range(100 - a):
        for c in range(100 - a - b):
            d = 100 - a - b - c

            score_total = 1
            calories_total = 0
            for x in range(5):
                sum_this = 0
                sum_this += scores[0][x] * a
                sum_this += scores[1][x] * b
                sum_this += scores[2][x] * c
                sum_this += scores[3][x] * d
                if sum_this < 0:
                    sum_this = 0
                if x == 4:
                    calories_total += sum_this
                else:
                    score_total *= sum_this
            if calories_total == 500:
                combos.append(score_total)

print(max(combos))
