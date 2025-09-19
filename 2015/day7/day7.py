def get_value(wire: str, circut: dict[str, str], memo: dict[str, int]) -> int:
    if wire.isdigit():
        return int(wire)

    if wire in memo:
        return memo[wire]

    parts: list[str] = circut[wire].split()

    val: int = 0

    if "AND" in parts:
        val = get_value(parts[0], circut, memo) & get_value(parts[2], circut, memo)
    elif "OR" in parts:
        val = get_value(parts[0], circut, memo) | get_value(parts[2], circut, memo)
    elif "LSHIFT" in parts:
        val = get_value(parts[0], circut, memo) << get_value(parts[2], circut, memo)
    elif "RSHIFT" in parts:
        val = get_value(parts[0], circut, memo) >> get_value(parts[2], circut, memo)
    elif "NOT" in parts:
        val = 65535 - get_value(parts[1], circut, memo)
    else:
        val = get_value(parts[0], circut, memo)

    memo[wire] = val
    return val


circut = {}

with open("input.txt", "r") as f:
    lines: list[str] = f.readlines()

for line in lines:
    input_string, output_wire = line.strip().split(" -> ")
    circut[output_wire] = input_string


def part_1():
    return get_value("a", circut, {})


def part_2():
    return get_value("a", circut, {"b": part_1()})


print(part_2())
