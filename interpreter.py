import sys
import threading
from enum import Enum
import instructions


def preprocess_code(code):
    code = code.replace("\n", "")
    code = code.split("d")
    cleaned_code = []
    for instruction in code:
        if instruction.startswith(" "):
            cleaned_code.append(instruction.lstrip())
            continue
        if not (instruction.startswith("/") or instruction == ""):
            cleaned_code.append(instruction)
            continue
    return cleaned_code


class InvalidCommandError(Exception):
    Message = "Invalid command error. Interpretation stopped"
    Code = 1


class FgplThread(threading.Thread):
    def ldi(self):
        self.program_counter += 1
        self.a = self.code[self.program_counter]
        self.program_counter += 1

    def lds(self):
        self.program_counter += 1
        self.a = self.space.get(int(self.code[self.program_counter]))
        self.program_counter += 1

    def ldr(self):
        self.program_counter += 1
        self.a = self.space.get(int(self.space[int(self.code[self.program_counter])]))
        self.program_counter += 1

    def sts(self):
        self.program_counter += 1
        self.space[int(self.code[self.program_counter])] = self.a
        self.program_counter += 1

    def str(self):
        self.program_counter += 1
        self.space[int(self.space[int(self.code[self.program_counter])])] = self.a
        self.program_counter += 1

    def chs(self):
        self.a = -int(self.a)
        self.program_counter += 1

    def add(self):
        self.program_counter += 1
        self.a = int(self.a) + int(self.space.get(int(self.code[self.program_counter])))
        self.program_counter += 1

    def sub(self):
        self.program_counter += 1
        self.a = int(self.a) - int(self.space.get(int(self.code[self.program_counter])))
        self.program_counter += 1

    def jmp(self):
        self.program_counter += 1
        self.program_counter = int(self.code[self.program_counter]) - 1

    def cpi(self):
        self.program_counter += 1
        if int(self.a) < int(self.code[self.program_counter]):
            self.c = -1
        elif int(self.a) > int(self.code[self.program_counter]):
            self.c = 1
        else:
            self.c = 0
        self.program_counter += 1

    def cpa(self):
        self.program_counter += 1
        if int(self.a) < int(self.space[int(self.code[self.program_counter])]):
            self.c = -1
        elif int(self.a) > int(self.space[int(self.code[self.program_counter])]):
            self.c = 1
        else:
            self.c = 0
        self.program_counter += 1

    def blt(self):
        self.program_counter += 1
        if self.c == -1:
            self.program_counter = int(self.code[self.program_counter]) - 1
        else:
            self.program_counter += 1

    def bgt(self):
        self.program_counter += 1
        if self.c == +1:
            self.program_counter = int(self.code[self.program_counter]) - 1
        else:
            self.program_counter += 1

    def beq(self):
        self.program_counter += 1
        if self.c == 0:
            self.program_counter = int(self.code[self.program_counter]) - 1
        else:
            self.program_counter += 1

    class States(Enum):
        new = 0
        no_error = 1
        stopped = 255

    def __init__(self, code, input_stream=sys.stdin, output_stream=sys.stdout):
        threading.Thread.__init__(self)
        instruction_lookup = {
            instructions.get_instruction_by_mnemonic("ldi").opcodes[0]: self.ldi,
            instructions.get_instruction_by_mnemonic("lds").opcodes[0]: self.lds,
            instructions.get_instruction_by_mnemonic("ldr").opcodes[0]: self.ldr,
            instructions.get_instruction_by_mnemonic("sts").opcodes[0]: self.sts,
            instructions.get_instruction_by_mnemonic("str").opcodes[0]: self.str,
            instructions.get_instruction_by_mnemonic("chs").opcodes[0]: self.chs,
            instructions.get_instruction_by_mnemonic("add").opcodes[0]: self.add,
            instructions.get_instruction_by_mnemonic("sub").opcodes[0]: self.sub,
            instructions.get_instruction_by_mnemonic("jmp").opcodes[0]: self.jmp,
            instructions.get_instruction_by_mnemonic("cpi").opcodes[0]: self.cpi,
            instructions.get_instruction_by_mnemonic("cpa").opcodes[0]: self.cpa,
            instructions.get_instruction_by_mnemonic("blt").opcodes[0]: self.blt,
            instructions.get_instruction_by_mnemonic("bgt").opcodes[0]: self.bgt,
            instructions.get_instruction_by_mnemonic("beq").opcodes[0]: self.beq
        }
        self.instruction_pointer = {}
        for instruction in instructions.instructions:
            for opcode in instruction.opcodes:
                self.instruction_pointer[opcode] = instruction_lookup.get(instruction.opcodes[0])
        self.a = 0
        self.c = 0
        self.program_counter = 0
        self.space = {}
        self.code = code
        self.state = FgplThread.States.new
        self.input_stream = input_stream
        self.output_stream = output_stream

    def step(self):
        self.instruction_pointer[self.code[self.program_counter]]()

    def stop(self):
        self.state = FgplThread.States.stopped
        self.program_counter = 0
        self.input_stream.close()
        self.output_stream.close()
        self.space = []

    def execute(self):
        self.state = FgplThread.States.no_error
        self.program_counter = 0
        while self.program_counter < len(self.code) and self.state == FgplThread.States.no_error:
            try:
                self.step()
            except(IndexError, KeyError):
                self.state = InvalidCommandError.Code
                raise InvalidCommandError(InvalidCommandError.Message)
        self.state = FgplThread.States.stopped

    def run(self):
        if self.state == FgplThread.States.new:
            self.execute()

    def __del__(self):
        self.stop()


if __name__ == "__main__":
    import signal

    signal.signal(signal.SIGINT, quit)
    program = []
    src_file_contents = ""
    try:
        src_file = open(sys.argv[1], "r")
        src_file_contents = src_file.readlines()
        src_file.close()
    except IndexError:
        print("Please supply source code file via program parameter.")
        exit(0)
    except FileNotFoundError:
        print("File not found error.", file=sys.stderr)
        exit(0)
    except PermissionError:
        print("Missing permissions to read source code file.", file=sys.stderr)
        exit(0)
    src_file_contents = "".join(src_file_contents)
    program = preprocess_code(src_file_contents)
    main_thread = FgplThread(program)
    main_thread.execute()

    # Debug!!!
    for address in main_thread.space.keys():
        print(str(address)+":", main_thread.space.get(address))
