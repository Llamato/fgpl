# fgpl The Fighting Game Programming Language

The programming language you can write with a fighting game controller.

## How it works

The language is basically an assembler like language. Each instruction has been assigned a fighting game controller compatible combo.
Address and value inputs are made using numpad notation. Each input is enterd / ended with a dust key press. Meaning the general syntax is as follows

operation combo followed by dust followed by parameters such as addresses or values terminated by dust

An example.
ldi 256 would be written as 4pd256d
meaning a key press combination of left punch for the instruction ldi followed by dust ending the input followed by the parameter down neutral right representing 256 followed by dust ending the command.

As of the writing of this document the following instructions are implemented.

| mnemonic  | input code / op code | Description                                 |
|-----------|----------------------|-------------------------------------------- |
| ldi value | 4pd(value)d          | Load an immediate value to register a       |
| lds addr  | 47kd(addr)d          | Load value at addr to register a            |
| ldr addr  | 41kd(addr)d          | Load value at address stored in addr into a |
| sts addr  | 69kd(addr)d          | Store value in a to addr                    |
| str addr  | 63kd(addr)d          | Store value in a at address stored in addr  |
| chs       | 456d/654d            | Change sign of number in a                  |
| add addr  | 632d(addr)d          | add value at addr to a                      |
| sub addr  | 412d(addr)d          | subtract value at addr from a               |
| jmp value | 7d/9d/1d/3d (value)d | set program counter to value                |
| cpi value | 741236985d(value)d   | compare value in a with value               |
| cpa addr  | 7896321475d(addr)d   | compare value at addr with value in a       |
| blt addr  | 654sd(addr)d         | branch if at last cp value in a was smaller |
| bgt addr  | 456sd6(addr)d        | branch if at last cp value in a was greater |
| beq addr  | 5sd(addr)d           | branch if at last cp values were equal      |

Thank you for reading.
Lamato / Tina
