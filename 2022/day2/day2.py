with open("day2/input.txt", "r") as f:
    input: list[str] = f.readlines()


def score(first: str, second: str) -> int:
    your_choice = {"X": "ZXY", "Y": "XYZ", "Z": "YZX"}[second]["ABC".index(first)]

    return ("XYZ".index(your_choice) + 1) + (
        3
        if "ABC".index(first) == "XYZ".index(your_choice)
        else (
            6
            if (first == "A" and your_choice == "Y")
            or (first == "B" and your_choice == "Z")
            or (first == "C" and your_choice == "X")
            else 0
        )
    )


print(sum(score(line[0], line[2]) for line in input))
# a, x = rock
# b, y = paper
# c, z = scissors
