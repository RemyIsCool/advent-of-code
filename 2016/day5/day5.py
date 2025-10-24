from hashlib import md5

with open("input.txt", "r") as f:
    puzzle_input = f.read().strip()

password = ["" for _ in range(8)]
i = 0
while "" in password:
    res = ""
    while not res.startswith("00000"):
        res = md5(str.encode(f"{puzzle_input}{i}")).hexdigest()
        i += 1
    if res[5] in map(str, range(8)) and password[int(res[5])] == "":
        password[int(res[5])] = res[6]
print("".join(password))
