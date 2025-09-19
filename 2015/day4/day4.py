from hashlib import md5

with open("input.txt", "r") as f:
    input = f.read()

count = 0
while True:
    hash = md5(f"{input}{count}".encode()).hexdigest()
    if hash.startswith("0" * 6):
        print(count)
        break
    count += 1
