from collections import defaultdict

with open("input.txt") as f:
    puzzle_input = f.read()

puzzle_input_lines = puzzle_input.splitlines()

numbers = []

for row, row_str in enumerate(puzzle_input_lines):
    current_number = 0
    current_number_start = (row, 0)

    for col, char in enumerate(row_str):
        if not char.isdigit():
            if current_number != 0:
                numbers.append((current_number, current_number_start))

            current_number = 0
            current_number_start = (row, col + 1)

            continue

        current_number = current_number * 10 + int(char)

    if current_number != 0:
        numbers.append((current_number, current_number_start))

part_numbers = defaultdict(list)

for number, (row, col) in numbers:
    number_digits = len(str(number))

    for x in range(number_digits):
        current_col = col + x

        done = False

        for d_row, d_col in (
            (x, y) for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0)
        ):
            other_char = "."
            nr, nc = row + d_row, current_col + d_col

            if (
                nr > 0
                and nr < len(puzzle_input_lines)
                and nc > 0
                and nc < len(puzzle_input_lines[0])
            ):
                other_char = puzzle_input_lines[nr][nc]

            if other_char == "*":
                part_numbers[(nr, nc)].append(number)
                done = True
                break

        if done:
            break


total = 0

for group in part_numbers.values():
    if len(group) <= 1:
        continue

    ratio = 1

    for elem in group:
        ratio *= elem

    total += ratio

print(total)
