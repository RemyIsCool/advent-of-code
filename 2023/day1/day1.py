import re


def to_digit_str(text):
    if text.isdigit():
        return text

    return str(
        [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ].index(text)
        + 1
    )


with open("input.txt", "r") as f:
    input = f.readlines()

numbers = []

for line in input:
    matches = set()
    for x in range(len(line)):
        matches |= {
            (match.start() + x, match.group())
            for match in re.finditer(
                r"\d|one|two|three|four|five|six|seven|eight|nine", line[x:]
            )
        }

    print(matches)

    first = min(matches, key=lambda m: m[0])[1]
    last = max(matches, key=lambda m: m[0])[1]

    numbers.append(int(to_digit_str(first) + to_digit_str(last)))
    print(numbers[-1])


print(sum(numbers))
