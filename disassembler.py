import sys
import instructions


def disassemble_op(opcode):
    opcode = opcode.split("/")[0]
    components = opcode.split(instructions.enter_key)
    components[0] = instructions.get_instruction_by_opcode(opcode)
    return " ".join(components)


def disassemble_all(opcodes):
    opcodes = opcodes.replace("\n", "")
    opcodes = opcodes.split(instructions.enter_key)
    mnemonics = []
    current_opcode = 0
    while current_opcode < len(opcodes):
        opcode = opcodes[current_opcode]
        if "/" in opcode:
            current_opcode = current_opcode + 1
            continue
        instruction = instructions.get_instruction_by_opcode(opcode)
        if instruction is None:
            current_opcode = current_opcode + 1
            continue
        mnemonic = instruction.mnemonic
        for current_operand in range(0, instruction.operants):
            current_opcode = current_opcode + 1
            mnemonic = mnemonic + " " + opcodes[current_opcode]
        mnemonics.append(mnemonic)
        current_opcode = current_opcode + 1
    return "\n".join(mnemonics)


if __name__ == "__main__":
    opcodes = []
    for line in sys.stdin:
        line = line.rstrip("\n")
        opcodes.append(line)
    opcodes = "".join(opcodes)
    mnemonics = disassemble_all(opcodes)
    print(mnemonics)
