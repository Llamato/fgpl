#Numbers are inputed though numpad alpabet with offsets for 5
#Each command is terminated by an (Enter / Dust) press

enter_key = "d"


class Instruction:
    def __init__(self, mnemonic, opcodes, operants, cycles):
        self.mnemonic = mnemonic
        self.opcodes = opcodes.split("/")
        self.operants = operants
        self.cycles = cycles
    pass


instructions = [
    Instruction("ldi", "4p", 1, 1),
    Instruction("lds", "47k", 1, 1),
    Instruction("ldr", "41k", 1, 1),
    Instruction("sts", "69k", 1, 1),
    Instruction("str", "63k", 1, 1),
    Instruction("chs", "456/654", 0, 1),
    Instruction("add", "632", 1, 1),
    Instruction("sub", "412", 1, 1),
    Instruction("jmp", "7/9/1/3", 1, 1),
    Instruction("cpi", "741236985", 1, 1),
    Instruction("cpa", "7896321475", 1, 1),
    Instruction("blt", "654s", 1, 1),
    Instruction("bgt", "456s", 1, 1),
    Instruction("beq", "5s", 1, 1)
]


def get_instruction_by_mnemonic(mnemonic):
    for instruction in instructions:
        if instruction.mnemonic == mnemonic:
            return instruction


def get_instruction_by_opcode(opcode):
    for instruction in instructions:
        for opcode_option in instruction.opcodes:
            if opcode_option == opcode:
                return instruction