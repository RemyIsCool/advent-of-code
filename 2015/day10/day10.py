from re import finditer


with open("input.txt", "r") as f:
    digits = f.read()

for _ in range(50):
    digits = "".join(
        f"{len(match.group(0))}{match.group(1)}"
        for match in finditer(r"(\d)\1*", digits)
    )

print(len(digits))
