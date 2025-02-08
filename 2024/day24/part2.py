with open("input.txt", "r") as f:
    input = f.read()

input_lines = input.strip().split("\n\n")
wires_lines, logic_lines = dict(), []

for line in input_lines[0].split("\n"):
    wire, val = line.split(":")
    wires_lines[wire] = int(val.strip())

for line in input_lines[1].split("\n"):
    wire1, op, wire2, _, wire3 = line.split(" ")
    if wire1 > wire2:
        wire1, wire2 = wire2, wire1
    logic_lines.append([wire1, wire2, op, wire3, 1, 0])

# I don't understand how this code works
answer = []
for logic in logic_lines:
    if logic[2] == "AND" and logic[0][0] == "x" and logic[1][0] == "y":  # Rule 1
        if logic[3][0] == "z" and logic[3] != "z00":
            answer.append(logic[3])
            logic[5] = 1
    elif (
        logic[2] == "XOR"
        and logic[0][0] != "x"
        and logic[1][0] != "y"
        and logic[3][0] != "z"
    ):  # Rule 2
        answer.append(logic[3])
        logic[5] = 1
    elif logic[3][0] == "z" and logic[2] != "XOR" and logic[3] != "z45":  # Rule 3
        answer.append(logic[3])
        logic[5] = 1
    if (
        logic[5] == 0
        and logic[2] == "AND"
        and logic[0][0] == "x"
        and logic[1][0] == "y"
        and logic[0] != "x00"
    ):  # Rule 4
        found = False
        for logic2 in logic_lines:
            if logic2[2] == "OR" and (logic[3] == logic2[0] or logic[3] == logic2[1]):
                found = True
        if found is not True:
            answer.append(logic[3])
    elif (
        logic[5] == 0
        and logic[2] == "XOR"
        and logic[0][0] == "x"
        and logic[1][0] == "y"
        and logic[0] != "x00"
    ):  # Rule 5
        found = False
        for logic2 in logic_lines:
            if logic2[2] == "AND" and (logic[3] == logic2[0] or logic[3] == logic2[1]):
                found = True
        if found is not True:
            answer.append(logic[3])


print(",".join(sorted(answer)))
