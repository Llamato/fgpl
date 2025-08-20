import instructions


class InvalidCommandError(Exception):
    Message = "Invalid command error. assembly stopped"
    Code = 1


def assemble_line(mnemonic):
    components = mnemonic.split(" ")
    instruction = instructions.get_instruction_by_mnemonic(components[0])
    try:
        components[0] = (instructions.enter_key + "/").join(instruction.opcodes)
    except AttributeError:
        raise InvalidCommandError

    opcode = instructions.enter_key.join(components)
    if len(instruction.opcodes) > 1:
        opcode = opcode.replace(instruction.opcodes[-1] + instructions.enter_key, instruction.opcodes[-1] + instructions.enter_key + " ")
    opcode = opcode + instructions.enter_key
    return opcode


def assemble_all(mnemonics):
    mnemonics = mnemonics.split("\n")
    opcodes = []
    for mnemonic in mnemonics:
        opcodes.append(assemble_line(mnemonic))
    return "\n".join(opcodes)


if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        line = line.rstrip("\n")
        print(assemble_line(line))
