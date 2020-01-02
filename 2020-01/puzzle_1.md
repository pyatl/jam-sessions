# Novice Puzzle: The Tyranny of the Rocket Equation

From Advent of Code 2019, Day 1: <https://adventofcode.com/2019/day/1>

Write your code in `puzzle_1.py`. The functions `part_1` and `part_2` will automatically be run when you click the "test" button. The `data` argument will hold the contents of the `puzzle_1.txt` file _as text_. You are free to create other functions, but don't rename or delete `part_1` and `part_2`.

If you are stuck, I've written some [tips](#tips) at the end.

### Part 1

Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs you to bring him measurements [...].

The Elves quickly load you into a spacecraft and prepare to launch. At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.

Fuel required to launch a given _module_ is based on its _mass_. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

- For a mass of `12`, divide by 3 and round down to get `4`, then subtract 2 to get `2`.
- For a mass of `14`, dividing by 3 and rounding down still yields `4`, so the fuel required is also `2`.
- For a mass of `1969`, the fuel required is `654`.
- For a mass of `100756`, the fuel required is `33583`.

The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input in `puzzle_1.txt`), then add together all the fuel values.

**What is the sum of the fuel requirements** for all of the modules on your spacecraft?

### Part 2

During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker stops the launch sequence. Apparently, you forgot to include additional fuel for the fuel you just added.

Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel _also_ requires fuel, and _that_ fuel requires fuel, and so on. Any mass that would require _negative fuel_ should instead be treated as if it requires _zero fuel_; the remaining mass, if any, is instead handled by _wishing really hard_, which has no mass and is outside the scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:

- A module of mass `14` requires `2` fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0, which would call for a negative fuel), so the total fuel required is still just `2`.
- At first, a module of mass `1969` requires `654` fuel. Then, this fuel requires `216` more fuel (`654 / 3 - 2`). `216` then requires `70` more fuel, which requires `21` fuel, which requires `5` fuel, which requires no further fuel. So, the total fuel required for a module of mass `1969` is `654 + 216 + 70 + 21 + 5 = 966`.
- The fuel required by a module of mass `100756` and its fuel is: `33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346`.

**What is the sum of the fuel requirements** for all of the modules on your spacecraft when also taking into account the mass of the added fuel? (Calculate the fuel requirements for each module separately, then add them all up at the end.)

### Tips

- It is always a good idea to try out Python code on the fly in a console. You can use one on your own laptop (like [IDLE](https://realpython.com/python-idle/)) or an online one (like [repl.it](https://repl.it/languages/python3)).

- To get the integral division of one number by another, you can use the `//` operator. This does the division _and_ rounds down the result!
  ```python
  >>> 3 / 2  # "True" division
  1.5
  >>> 3 // 2  # Integral division
  1
  >>> 1969 // 3
  656
  ```

- Remember that the input data will be provided as text. Here are a few tools you could use:
  - The `.splitlines()` method of string objects, which returns a list of lines:
    ```python
    >>> string = "1\n2\n3"
    >>> print(string)
    1
    2
    3
    >>> string.splitlines()
    ['1', '2', '3']
    ```
  - The `int` type builtin can be called to convert a string into a number:
    ```python
    >>> int("1234")
    1234
    ```

- The two main constructs you will need for this problem are:
  - The `for` loop, that goes over every item of a collection in order. E.g.:
    ```python
    total = 0
    for number in range(10):
        total += number
        print(total)
    ```
  - The `while` loop (for part 2 in particular), that repeats until the given condition is no longer true. E.g.:
    ```python
    number = 10
    while number >= 0:
        print(number)
        number -= 1
    ```
 