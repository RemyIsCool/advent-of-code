puzzle_input = input()
count = int(puzzle_input)

elf_1 = 0
elf_2 = 1

scores = [3, 7]


def make_recipes():
    global elf_1, elf_2, scores
    new_score = scores[elf_1] + scores[elf_2]

    scores.extend(map(int, str(new_score)))

    elf_1 = (elf_1 + scores[elf_1] + 1) % len(scores)
    elf_2 = (elf_2 + scores[elf_2] + 1) % len(scores)


def part1():
    while len(scores) < count:
        make_recipes()

    for _ in range(10):
        make_recipes()

    print("Part 1:")
    print("".join(map(str, scores[count : count + 10])))
    print()


def part2():
    input_length = len(puzzle_input)
    input_first_digit = int(puzzle_input[0])
    while (
        len(scores) < input_length
        or scores[-input_length] != input_first_digit
        or any(x != int(puzzle_input[i]) for i, x in enumerate(scores[-input_length:]))
    ):
        make_recipes()

    print("Part 2:")

    print(len(scores[: "".join(map(str, scores)).index(puzzle_input)]))


part1()
part2()
