with open("day4/input.txt", "r") as f:
    input = f.readlines()

answer_1 = 0
answer_2 = 0

for line in input:
    first, second = line.split(",")

    first_start, first_end = map(int, first.split("-"))
    second_start, second_end = map(int, second.split("-"))

    if (first_start >= second_start and first_end <= second_end) or (
        second_start >= first_start and second_end <= first_end
    ):
        answer_1 += 1

    if set(range(first_start, first_end + 1)) & set(
        range(second_start, second_end + 1)
    ):
        answer_2 += 1

print(answer_1, answer_2)
