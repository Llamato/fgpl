# fgpl The Fighting Game Programming Language

FGPL was created to answer one simple question. Can you make a programming language you can write with an arcade stick or an all button controller typically used to play fighting games.

## How it works

The language is basically an assembler like language. Each instuction has been assigned a fighting game controller compatible combo.
Address and value inputs are made using numpad notation. Each input is enterd / ended with a dust key press. Meaning the general syntax is as follows

operation combo followed by dust followed by parameters such as addresses or values terminated by dust

An example.
ldi 256 would be written as 4pd256d
meaing a key press combination of left punch for the instruction ldi followed by dust ending the input followed by the parameter down neutral right representing 256 followed by dust ending the command.

As of the writing of this document the following instructions are implemented.

| mnemonic  | input code / op code | Description                                 |
|-----------|----------------------|-------------------------------------------- |
| ldi value | 4pd(value)d          | Load an imidate value to register a         |
| lds addr  | 47kd(addr)d          | Load value at addr to register a            |
| ldr addr  | 41kd(addr)d          | Load value at address stored in addr into a |
| sts addr  | 69kd(addr)d          | Store value in a to addr                    |
| str addr  | 63kd(addr)d          | Store value in a at address stored in addr  |
| chs       | 456d/654d            | Change sign of number in a                  |
| add addr  | 632d(addr)d          | add value at addr to a                      |
| sub addr  | 412d(addr)d          | subtract value at addr from a               |
| jmp value | 7d/9d/1d/3d (value)d | set programm counter to value               |
| cpi value | 741236985d(value)d   | compare value in a with value               |
| cpa addr  | 7896321475d(addr)d   | compare value at addr with value in a       |
| blt addr  | 654sd(addr)d         | branch if at last cp value in a was smaller |
| bgt addr  | 456sd6(addr)d        | branch if at last cp value in a was greater |
| beq addr  | 5sd(addr)d           | branch if at last cp values were equal      |

More instuctions will be added. (I hope). I am also currently expiremnting with a better way to input numbers as some input combos are next to impossible with a fighting game controller. 91 for example would become 951 making the number 91 impossible to enter. As soon as I found a good soultion the programming language will be updated.

If you got any suggestions as on how to improve this language please let me know.
Code contribuitons are also very welcome.

Thank you for reading.
Lamato / Tina
