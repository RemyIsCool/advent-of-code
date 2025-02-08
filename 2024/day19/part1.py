with open("input.txt", "r") as f:
    towels_str, patterns_str = f.read().split("\n\n")

towels = towels_str.split(", ")
patterns = patterns_str.splitlines()

longest_towel = max(map(len, towels))


def get_starting_towels(pattern_start: str) -> list[str]:
    starting_towels: list[str] = []

    for x in range(1, len(pattern_start) + 1):
        chunk = pattern_start[:x]
        if chunk in towels:
            starting_towels.append(chunk)

    return starting_towels


def is_possible(pattern: str):
    if pattern in towels:
        return True

    starting_towels = get_starting_towels(pattern[:longest_towel])

    if not starting_towels:
        return False

    for towel in starting_towels:
        if is_possible(pattern[len(towel) :]):
            return True

    return False


answer = 0

for pattern in patterns:
    if is_possible(pattern):
        answer += 1

print(answer)
