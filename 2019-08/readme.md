
# EXAPUNKS Emulator

PyATL Jam Session — August 1st 2019

## Introduction

[EXAPUNKS] is a 2018 video game by Zachtronics. It is set in a cyberpunk past
where all technology works using swarms of small programs, known as EXAs
(EXecution Agents). The principle of the game is to program your EXAs using an
assembly-like language, and accomplish various (illicit) jobs. It is a
challenging but accessible and immersive game, and I strongly recommend trying
it out.

For today's coding challenge, we will be building a simulator that can read and
execute a program written in the EXA language.

[EXAPUNKS]: http://www.zachtronics.com/exapunks/

_Disclaimer: EXAPUNKS and its contents, including the EXA language and the
excerpts from the TRASH WORLD NEWS manual used in this document, are a
property of Zachtronics LLC._

## EXA fundamentals

Following the tradition of Zachtronics' previous programming games, the manual
of EXAPUNKS is a core element of the gameplay (and you're encouraged to print
it on physical paper). Let's refer to the said manual (or, as it calls itself,
_TRASH WORLD NEWS issue 1_) for some explanations:

> Every EXA contains **code** and **registers**.  
> **CODE:** This is a list of instructions that tell an EXA what to do. It's
> written in a special computer language specifically designed for them. We'll
> dig into the language in the following sections.   
> **REGISTERS:** Think of these are slots that can store numbers. Registers
> can be read and written to by instructions in your code. 

An EXA has three registers:

* The `X` register is a general-purpose storage register. It can store a
  number and initially contains 0.
* The `T` register is a general-purpose storage register like `X`. It is also
  the destination for `TEST` instructions ([challenge #2]), and is the
  criterion for conditional jumps ([challenge #3]).
* A file handling register named `F`. Its operation will be detailed in
  [challenge #4].

Through every instruction description in this challenge, the following
abbreviations will be used to represent required operands:

* `R`: A register
* `R/N`: A register, or a number between -9999 and 9999
* `L`: A label defined by a `MARK` pseudo-instruction (see [challenge #3])

## Challenge 1: Basic operations

### Instructions

For the first part of the problem, we will be focusing on the very basic
features of the language, such as registers and arithmetics:

* `COPY R/N R`  
  Copy the value of the first operand into the second operand.
* `ADDI R/N R/N R`  
  Add the value of the first operand to the value of the second operand and
  store the result in the third operand.
* `SUBI R/N R/N R`  
  Same as `ADDI`, for substraction.
* `MULI R/N R/N R`  
  Same as `ADDI`, for multiplication.
* `DIVI R/N R/N R`  
  Same as `ADDI`, for integral division.
* `MODI R/N R/N R`  
  Same as `ADDI`, for modulo.

Here are a few parsing constraints:
* Any unknown instruction, register or invalid number should result in a crash
* Leading spaces (at the start of a line of code) should be safely ignored
* Empty lines should be ignored

Write a program that can understand a piece of code with any of the above
instructions and run it.

### Guidelines

If you are relatively new to programming, this could be a steep challenge to
get into. Here are a few ideas to help you start out:

1. It is generally a good idea to start by identifying the inputs and outputs
   of the program. Here, the input is the code for the EXA, which will be just
   plain text. No need to worry about outputs for now; printing the register
   values after each step should be enough. Don't hesitate to add more `print`
   lines as needed.

2. The first piece of code you'll need is one that can read a line of EXA code
   and make sense of it. For example, `"ADDI 30 X T"` could be converted into
   `("ADDI", [30, "X", "T"])` or any other structure of your choice. This will
   make it much easier to write the actual running logic. It is at this step
   that you could check if instructions and their operands are valid.

3. Before implementing the instructions, think about how you want to handle
   the registers. Here are some suggestions:
   * Just have the registers as variables.
   * Go for an object-oriented approach, where `X` and `T` are attributes of
     your EXA object.
   * Go for a functional approach, where the current register values (or state
     in general) is passed to instructions; those then return a new state.

4. If you manage to design the code parsing and register handling carefully,
   actually implementing the instructions should be fairly easy! The only
   detail is that you will need to be careful about whether an argument is a
   number or a register name when both are allowed, and choose the correct
   behavior.

### Example

Here is an example:

    COPY 70 X
    ADDI X 1 X
    COPY 3 T
    MULI T X T
    SUBI T 1 T

Decomposed, this program will:

1. Set `X` to 70
2. Add 1 to the value of `X` and store that value back in `X`
3. Set `T` to 3
4. Multiply `X` by `T` and store that value in `T`
5. Substract 1 from `T` and store the result in `T`

At the end, `X` should hold 71 and `T` should hold 212.

### Challenge

Here is another example for you to try your code on:

    COPY 647 X
    MODI X 7 T
    DIVI X T X
    MULI T T T
    MULI X T X
    MULI T T T
    ADDI X T X
    DIVI T 10 T
    ADDI X 3 X
    ADDI T X T
    ADDI T X X
    SUBI X T T
    SUBI X T X
    SUBI X T X

What are the values of the registers at the end? As a bonus, can you identify
what operation the last five instructions are effectively doing?

## Challenge 2: Tests
[challenge #2]: #challenge-2-tests

I mentionned earlier that the `T` register was used for tests. This part of
the challenge will be to program the `TEST` instruction:

* `TEST R/N = R/N`  
  Compare the value of the first operand to the value of the second operand.
  If they are equal, set the `T` register to 1, otherwise set the `T` register
  to 0. The same syntax is used for the `<` (less than) and `>` (greater than)
  tests. 

Here is an example of `TEST`:

    COPY 10 X
    COPY X T
    TEST X = T
    SUBI X T T
    TEST X > T
    TEST T < 1

This will:

1. Set `X` to 10
2. Set `T` to the value of `X`
3. Test if `X` and `T` are equal. This is true, so `T` is set to 1.
4. Substract `T` from `X`, store it in `T` (now 9).
5. Test if `X` is greater than `T`. This is true again, `T` is set to 1.
6. Finally, test if `T` is smaller than 1. This is false, so `T` is set to 0.

So far it might not look very useful, but the next challenge will fix that.

## Challenge 3: Labels and Jumps
[challenge #3]: #challenge-3-labels-and-jumps

### Instructions

So far our program pointer only moves through the program from top to bottom,
and doen't have much in the way of actual logic. Time to introduce some useful
flow control instrustions:

* `MARK L`  
  Mark this line with the specified label. `MARK` is a pseudo-instruction and
  is not executed.
* `JUMP L`  
  Jump to the specified label.
* `TJMP L`  
  Jump to the specified label if the `T` register equals 1 (or any value other
  than 0). This corresponds to a `TEST` result that was true.
* `FJMP L`  
  Jump to the specified label if the `T` register equals 0. This corresponds
  to a `TEST` result that was false.

If the same label is marked multiple times, the program is entirely invalid
and should fail to parse or compile.

*Note:* Be careful to not write any infinite loops!

### Example

Let me walk you through a simple example:

    COPY 1 X
    COPY 7 T
    MARK LOOP
    MULI T X X
    SUBI T 1 T
    TJMP LOOP

1. Set `X` to 1
2. Set `T` to 7.
3. Line 4 gets marked as `LOOP`.
4. Multiply `X` by `T` and store that in `X`.
5. Decrease `T` by 1.
6. If the value of `T` is not 0, jump back to `LOOP` (step 4.).

This effectively calculates 7! ([factorial] of 7), which should be 5040.

[factorial]: https://en.wikipedia.org/wiki/Factorial

### Challenge

Can you implement a program that tests the [Collatz conjecture] for a number
of your choice? It doesn't need to output the number of steps or anything, for
now try to implement a program that goes through the sequence until it ends.

[Collatz conjecture]: https://en.wikipedia.org/wiki/Collatz_conjecture

## Challenge 4: File handling
[challenge #4]: #challenge-4-file-handling

### Instructions

All that programming is no good if it cannot input and output. Thankfully, EXAs
can manipulate files and leave traces.

In our simplified emulator, a file is simply a list of numbers with a name.
To use a file, an EXA must first grab that file by its name. Once done, it has
to drop it before using a different file.

Here is also where the `F` register comes in play. The reference guide reads:

> The `F` register allows an EXA to read and write the contents of a held file.
> When an EXA grabs a file, its "file cursor" will be set to the first value in
> the file. Reading from the `F` register will read this value; writing to the
> `F` register will overwrite this value. After reading or writing the `F`
> register, the file cursor will automatically advance. Writing to the end of
> the file will append a new value instead of overwriting.

*Note:* This is **not** the same file handling as the one you'd do with `open`
in Python. These files are virtual; lists which exist only in the emulator.
You will need to add them to your simulation.

The file manipulation instructions to implement are:

* `GRAB R/N`  
  Grab a file with the specified ID.
* `FILE R`  
  Copy the ID of the file into the specified register.
* `SEEK R/N`  
  Move the file cursor forward (positive) or backwards (negative) by the
  specified number of values.  
  If `SEEK` would move the file cursor past the biginning or end of the file
  it will instead be clamped. Thus, you can use values of -9999 or 9999 to
  reliably move to the beginning or end of a file.
* `VOID F`  
  Remove the value highlighted by the file cursor from the currently held file.
* `DROP`  
  Drop the currently held file.
* `TEST EOF`  
  If the file pointer is currently at the end of the held file, set the `T`
  register to 1, otherwise set the `T` register to 0. 

Note that trying to access this register when the EXA isn't holding a file will
result in an "Invalid `F` register access" error, causing the EXA to crash and
terminate. If an EXA tries to open a file that does not exist (or is otherwise
not available), it also crashes.

Modify your emulator to support file handling. On top of the code to run, it
will need to be initialized with files (and their contents). It will need to
return the file contents at the end of execution.

### Example

Let's look at a simple file handling program. In this scenario, the environment
starts with two existing files: one called 100 with a list of numbers, and a
second one called 200 that's empty.

    GRAB 100
    MARK FILE_READ
    ADDI F X X
    TEST EOF
    FJMP FILE_READ
    DROP
    GRAB 200
    COPY X F
    DROP

This time, try to walk through the instructions yourself. This script reads the
numbers in 100, sums them, and writes the sum to 200.

### Final Challenge

Here's the final code I want you to test your emulator against. The virtual
world is expected to contain a file with the ID 400 that is initially empty.

    GRAB 400
    COPY 1 X
    MARK A
    SEEK -9999
    ADDI X 1 X
    TEST X < 50
    FJMP D
    MARK B
    TEST EOF
    TJMP C
    MODI X F T
    FJMP A
    JUMP B
    MARK C
    COPY X F
    JUMP A
    MARK D
    DROP

What are the contents of the file 400 at the end of the program? Can you
identify what calculation this program is doing?

## Bonus

If you enjoyed playing with the EXA language, then once again I recommend
purchasing and playing [EXAPUNKS]. In the real game, a single EXA is only
_one_ of potentially _many_ interconnected EXAs! This adds a whole new level
of richness to the idea, of which these challenges only scratched the surface.
Zachtronics' world of EXAs has a lot more to offer.

If you're already an EXAPUNK veteran, you will have already noticed the
simplifications made in this exercise. Here are some more advanced features
you could implement from the game:

* Support for other misc instructions (`SWIZ`, `HALT`, `NOTE`, `NOOP`, `RAND`)
* `@` macro instructions for code repetition
* Simulation of hosts and movement with `LINK` and `HOST`
* Support for keyword values (a.k.a. strings)
* Support for `MAKE` and `DROP` (create/delete files)
* Support for hardware registers (read-only or write-only)
* Accurate runtime errors
* And the ultimate challenge: proper full EXA-VM simulation
  * Have swarms of EXAs with their programs properly in sync
  * `REPL` and `KILL` support for forking and termination
  * Support for the `M` register and `MODE`

