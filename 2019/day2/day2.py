with open("input.txt", "r") as file:
    input = list(map(int, file.read().strip().split(",")))


def run_program(program):
    pointer = 0

    while True:
        opcode = program[pointer]

        if opcode == 99:
            break
        elif opcode == 1:
            program[program[pointer + 3]] = program[program[pointer + 1]] + program[program[pointer + 2]]
        elif opcode == 2:
            program[program[pointer + 3]] = program[program[pointer + 1]] * program[program[pointer + 2]]
        
        pointer += 4

    return program


print("Part 1", run_program(input.copy())[0])


for noun in range(100):
    for verb in range(100):
        program = input.copy()
        program[1] = noun
        program[2] = verb
        if run_program(program)[0] == 19690720:
            print("Part 2", 100 * noun + verb)
            break
    else:
        continue
    break