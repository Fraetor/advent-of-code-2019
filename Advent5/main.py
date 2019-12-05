input_file = open("input", "r")
default_memory = [int(i) for i in input_file.read().split(",")]
input_file.close()


def mode_handler(mode, digit, value):
    try:
        if mode[digit] == "0":
            return memory[value]
        elif mode[digit] == "1":
            return value
        else:
            print("Unhandled mode error (d:{}, v:{})".format(digit, value))
            exit(1)
    except IndexError:
        return memory[value]


def opcode1(a, b, c, mode):  # Add
    memory[c] = mode_handler(mode, -1, a) + mode_handler(mode, -2, b)


def opcode2(a, b, c, mode):  # Multiply
    memory[c] = mode_handler(mode, -1, a) * mode_handler(mode, -2, b)


def opcode3(a):  # Input
    memory[a] = int(input("Please enter an integer: "))


def opcode4(a, mode):  # Output
    print(mode_handler(mode, -1, a))


def opcode5(a, b, mode):  # Jump-if-true
    if mode_handler(mode, -1, a) != 0:
        return mode_handler(mode, -2, b)
    else:
        return 0


def opcode6(a, b, mode):  # Jump-if-false
    if mode_handler(mode, -1, a) == 0:
        return mode_handler(mode, -2, b)
    else:
        return 0


def opcode7(a, b, c, mode):  # Less than
    if mode_handler(mode, -1, a) < mode_handler(mode, -2, b):
        memory[c] = 1
    else:
        memory[c] = 0


def opcode8(a, b, c, mode):  # Equals
    if mode_handler(mode, -1, a) == mode_handler(mode, -2, b):
        memory[c] = 1
    else:
        memory[c] = 0


def opcode99():  # Exit
    pass


def interpreter():
    pointer = 0
    while True:
        # print(",".join(str(integer) for integer in memory))
        if str(memory[pointer])[-2:] == "01" or str(memory[pointer])[-2:] == "1":
            opcode1(memory[pointer + 1], memory[pointer + 2], memory[pointer + 3], str(memory[pointer])[:-2])
            pointer += 4
        elif str(memory[pointer])[-2:] == "02" or str(memory[pointer])[-2:] == "2":
            opcode2(memory[pointer + 1], memory[pointer + 2], memory[pointer + 3], str(memory[pointer])[:-2])
            pointer += 4
        elif str(memory[pointer])[-2:] == "03" or str(memory[pointer])[-2:] == "3":
            opcode3(memory[pointer + 1])
            pointer += 2
        elif str(memory[pointer])[-2:] == "04" or str(memory[pointer])[-2:] == "4":
            opcode4(memory[pointer + 1], str(memory[pointer])[:-2])
            pointer += 2
        elif str(memory[pointer])[-2:] == "05" or str(memory[pointer])[-2:] == "5":
            pointer_jmp = opcode5(memory[pointer + 1], memory[pointer + 2], str(memory[pointer])[:-2])
            if pointer_jmp == 0:
                pointer += 3
            else:
                pointer = pointer_jmp
        elif str(memory[pointer])[-2:] == "06" or str(memory[pointer])[-2:] == "6":
            pointer_jmp = opcode6(memory[pointer + 1], memory[pointer + 2], str(memory[pointer])[:-2])
            if pointer_jmp == 0:
                pointer += 3
            else:
                pointer = pointer_jmp
        elif str(memory[pointer])[-2:] == "07" or str(memory[pointer])[-2:] == "7":
            opcode7(memory[pointer + 1], memory[pointer + 2], memory[pointer + 3], str(memory[pointer])[:-2])
            pointer += 2
        elif str(memory[pointer])[-2:] == "08" or str(memory[pointer])[-2:] == "8":
            opcode8(memory[pointer + 1], memory[pointer + 2], memory[pointer + 3], str(memory[pointer])[:-2])
            pointer += 2
        elif str(memory[pointer])[-2:] == "99":
            opcode99()
            break
        else:
            print("Invalid opcode encountered at position {}. Memory: {}".format(pointer, memory[pointer]))
            exit(1)


memory = default_memory[:]

interpreter()