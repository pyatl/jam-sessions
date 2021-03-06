## Challenging Puzzle: Some Assembly Required

From Advent of Code 2015, Day 7: <https://adventofcode.com/2015/day/7>

Write your code in `puzzle_4.py`. The functions `part_1` and `part_2` will automatically be provided with the puzzle input from `puzzle_4.txt`, as a list of strings (one line per item).

### Part 1

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from `0` to `65535`). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: `x AND y -> z` means to connect wires `x` and `y` to an AND gate, and then connect its output to wire `z`.

For example:

- `123 -> x` means that the signal `123` is provided to wire `x`.
- `x AND y -> z` means that the bitwise AND of wire `x` and wire `y` is provided to wire `z`.
- `p LSHIFT 2 -> q` means that the value from wire `p` is left-shifted by `2` and then provided to wire `q`.
- `NOT e -> f` means that the bitwise complement of the value from wire `e` is provided to wire `f`.

Other possible gates include `OR` (bitwise OR) and `RSHIFT` (right-shift). If, for some reason, you'd like to **emulate** the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

    123 -> x
    456 -> y
    x AND y -> d
    x OR y -> e
    x LSHIFT 2 -> f
    y RSHIFT 2 -> g
    NOT x -> h
    NOT y -> i

After it is run, these are the signals on the wires:

    d: 72
    e: 507
    f: 492
    g: 114
    h: 65412
    i: 65079
    x: 123
    y: 456

In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire `a`?

### Part 2

Now, take the signal you got on wire `a`, override wire `b` to that signal, and reset the other wires (including wire `a`). What new signal is ultimately provided to wire `a`?

### Tips

* Despite the appearances, this is **not** an assembly-like language to execute. Each wire will only have one line defining what it is connected to. So when you're asked to find the value of wire `a`, you need to look up where it's defined and work your way down the definitions from there.

* Don't forget that values are 16-bit unsigned. You cannot store indefinitely large numbers.

* I'd be very interested in seeing a non-recursive solution to this.
