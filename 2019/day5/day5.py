with open("input.txt", "r") as file:
    input = list(map(int, file.read().strip().split(",")))


def run_program(program):
    pointer = 0

    while True:
        opcode = program[pointer]

        match opcode:
            case 99:
                break
            case 1:
                program[program[pointer + 3]] = (
                    program[program[pointer + 1]] + program[program[pointer + 2]]
                )
            case 2:
                program[program[pointer + 3]] = (
                    program[program[pointer + 1]] * program[program[pointer + 2]]
                )
            case 3:
                pass

        pointer += 4

    return program
