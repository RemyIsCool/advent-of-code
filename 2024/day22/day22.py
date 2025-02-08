from collections import defaultdict

with open("input.txt", "r") as f:
    input = f.readlines()

input_numbers = [int(num.strip()) for num in input]


Diffs = tuple[int, int, int, int]

sequences: defaultdict[Diffs, int] = defaultdict(int)

for number in input_numbers:
    prices: list[int] = [number % 10]

    for _ in range(2000):
        number ^= number * 64
        number %= 16777216

        number ^= number // 32
        number %= 16777216

        number ^= number * 2048
        number %= 16777216

        prices.append(number % 10)

    diffs: list[int] = []

    for p, n in zip(prices, prices[1:]):
        diffs.append(n - p)

    monkey = list(zip(diffs, prices[1:]))

    seen: set[Diffs] = set()

    for (((diff1, _), (diff2, _)), (diff3, _)), (diff4, price4) in zip(
        zip(zip(monkey, monkey[1:]), monkey[2:]), monkey[3:]
    ):
        s = (diff1, diff2, diff3, diff4)
        if s in seen:
            continue
        seen.add(s)
        sequences[s] += price4


print(sequences[max(sequences, key=sequences.get)])  # type: ignore
