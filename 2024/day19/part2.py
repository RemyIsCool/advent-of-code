from functools import cache

with open("input.txt", "r") as f:
    towels_str, patterns_str = f.read().split("\n\n")


towels = towels_str.split(", ")
patterns = patterns_str.splitlines()

longest_towel = max(map(len, towels))


@cache
def get_starting_towels(pattern_start: str) -> list[str]:
    starting_towels: list[str] = []

    for x in range(1, len(pattern_start) + 1):
        chunk = pattern_start[:x]
        if chunk in towels:
            starting_towels.append(chunk)

    return starting_towels


@cache
def combination_count(pattern: str, depth=0) -> int:
    starting_towels = get_starting_towels(pattern[:longest_towel])

    if not starting_towels:
        return 0

    count = 0

    for towel in starting_towels:
        combinations = combination_count(pattern[len(towel) :], depth + 1)

        count += combinations

    if pattern in towels:
        count += 1

    return count


answer = 0

for pattern in patterns:
    answer += combination_count(pattern)

print(answer)
