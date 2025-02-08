with open("input.txt", "r") as f:
    input = f.read()


values_str, connections_str = input.split("\n\n")

values: dict[str, int] = {}

for line in values_str.splitlines():
    name, value = line.split(": ")
    values[name] = int(value)


queue = connections_str.splitlines()

while queue:
    connection = queue.pop(0)

    inputs, output = connection.split(" -> ")

    first_input, operand, second_input = inputs.split(" ")

    if first_input not in values or second_input not in values:
        queue.append(connection)
        continue

    match operand:
        case "OR":
            values[output] = values[first_input] | values[second_input]

        case "AND":
            values[output] = values[first_input] & values[second_input]

        case "XOR":
            values[output] = values[first_input] ^ values[second_input]


z_values = [
    str(value)
    for key, value in sorted(
        values.items(),
        key=lambda item: -int(item[0][1:]) if item[0][1:].isdigit() else -1,
    )
    if key[0] == "z"
]

print(int("".join(z_values), 2))
