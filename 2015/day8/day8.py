def calculate_difference(string: str) -> int:
    original_len = len(string.strip())
    to_process: str = string.strip()[1:-1]
    pointer: int = 0
    size: int = 0

    while pointer < len(to_process):
        if to_process[pointer] != "\\":
            pointer += 1
            size += 1
            continue

        if to_process[pointer + 1] == "\\":
            pointer += 2
            size += 1
            continue

        if to_process[pointer + 1] == "x":
            pointer += 4
            size += 1
            continue

        pointer += 2
        size += 1

    return original_len - size


def calculate_encoded_difference(string: str) -> int:
    return len(encode_string(string)) - len(string.strip())


def encode_string(string: str) -> str:
    return f'"{string.strip().replace("\\", "\\\\").replace('"', '\\"')}"'


with open("input.txt", "r") as f:
    strings: list[str] = f.readlines()

answer = sum(map(calculate_encoded_difference, strings))
print(answer)
