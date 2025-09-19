from re import finditer


with open("input.txt", "r") as f:
    input_file = f.read()

replacements, text = input_file.split("\n\n")
replacements = sorted(
    [line.split(" => ") for line in replacements.splitlines()], key=lambda x: -len(x[1])
)


def shrink(molecule, count):
    if molecule == "e":
        return count

    options = set()

    for end, start in replacements:
        for match in finditer(start, molecule):
            shrunken = molecule[: match.start()] + end + molecule[match.end() :]
            options.add(shrunken)

    if len(options) == 0:
        return

    for option in options:
        res = shrink(option, count + 1)
        if res:
            return res


print(shrink(text, 0))
