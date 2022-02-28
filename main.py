def compile(program):
    memory = {"MEM_POINTER": 0}
    instructions = program
    instruct_pointer = 0
    while True:
        if len(instructions) == instruct_pointer:
            break
        disassemble = instructions[instruct_pointer].split(" ")
        memory["MEM_POINTER"] = instruct_pointer
        if disassemble[0] == "mov":
            if disassemble[2] in memory:
                if disassemble[1] == "MEM_POINTER":
                    continue
                memory[disassemble[1]] = memory[disassemble[2]]
            else:
                memory[disassemble[1]] = int(disassemble[2])
        elif disassemble[0] == "inc":
            if disassemble[1] in memory:
                if disassemble[1] == "MEM_POINTER":
                    continue
                memory[disassemble[1]] += 1
            else:
                pass
        elif disassemble[0] == "dec":
            if disassemble[1] in memory:
                if disassemble[1] == "MEM_POINTER":
                    continue
                memory[disassemble[1]] -= 1
            else:
                pass
        elif disassemble[0] == "jnz":
            if disassemble[1] in memory:
                if memory[disassemble[1]] != 0:
                    instruct_pointer += int(disassemble[2])
                    continue
            else:
                if disassemble[1] != 0:
                    instruct_pointer += int(disassemble[2])
                    continue
        elif disassemble[0] == "del":
            if disassemble[1] in memory:
                del memory[disassemble[1]]
            else:
                pass
        instruct_pointer += 1
    return memory


stack = []


def var(name, value):
    stack.append(f"mov {name} {value}")


def multiply(value1, value2, moveto):
    stack.append(f"mov MULT_RESULT 0")
    stack.append(f"mov MULT_Y {value2}")
    stack.append(f"mov MULT_X {value1}")
    stack.append("inc MULT_RESULT")
    stack.append("dec MULT_X")
    stack.append("jnz MULT_X -2")
    stack.append("dec MULT_Y")
    stack.append("jnz MULT_Y -5")
    stack.append("del MULT_X")
    stack.append("del MULT_Y")
    stack.append(f"mov MULT_RESULT {moveto}")
