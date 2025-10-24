from collections import defaultdict
from string import ascii_lowercase

with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0

for line in lines:
    parts = line.split("-")

    id = int(parts[-1][:3])

    letters = defaultdict(int)
    decrypted = ""
    for char in "".join(parts[:-1]):
        letters[char] += 1
        decrypted += ascii_lowercase[
            (ascii_lowercase.index(char) + id) % len(ascii_lowercase)
        ]
    if decrypted == "northpoleobjectstorage":
        print(id)

    common = map(
        lambda c: c[0],
        sorted(sorted(letters.items()), key=lambda c: -c[1])[:5],
    )

    check = parts[-1][4:-2]
    if "".join(common) == check:
        total += id

print(total)
