with open("input.txt", "r") as f:
    aunts_sue = f.readlines()


target_values = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


for aunt_sue in aunts_sue:
    key, values = aunt_sue.strip().split(": ", 1)
    number = key[4:]
    values = values.split(", ")
    values_dict = {}

    for value in values:
        name, num = value.split(": ")
        values_dict[name] = int(num)

    valid = True
    for key, value in target_values.items():
        if key not in values_dict:
            continue

        if key in ["cats", "trees"]:
            if values_dict[key] <= value:
                valid = False
                break
        elif key in ["pomeranians", "goldfish"]:
            if values_dict[key] >= value:
                valid = False
                break
        else:
            if values_dict[key] != value:
                valid = False
                break

    if valid:
        print(number)
        break
