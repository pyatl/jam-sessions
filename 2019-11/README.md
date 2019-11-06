
# December's Close Enough

PyATL Jam Session — November 7th, 2019

#### Credits

All puzzles (and their input) are from [adventofcode.com][aoc], and designed by Eric Wastl.

## Instructions

See our starting up guide at:  
<https://github.com/pyatl/jam-sessions/wiki/Cyber-Dojo-Instructions>

## Introduction

December is only a few weeks away! And with December comes the Advent... of code!

[Advent of Code][aoc] is a yearly event organized by Eric Wastl, where a programming puzzle is published every day from December 1st through December 25th. It will run for the fifth time this year.

Its puzzles are fun, interesting, and all excellently written. This month we will look at a few of the easier puzzles from the 2015 edition. The instructions and input are reproduced here for convenience, along with some tips. But feel free to work from the official website if you wish.

#### More about Advent of Code

The preferred way to participate is to create an account on [the website][aoc]: puzzle inputs are individually generated, consequently each contestant will be submitting a different answer. The game is also a competition, ranking players by speed. 

But nobody's forcing you to compete. All puzzles are available online without the need to create an account. They are great challenges and a good learning tool! The problems can also be solved using any language; doing Advent of Code problems multiple times with different languages is an excellent way to learn and appreciate the strengths and particularities of each.

**Warning:** while the first few puzzles of each year are generally quite easy, the difficulty gets much steeper over time. If you're a beginner, puzzles from the second week onwards will likely be very challenging.

[aoc]: https://adventofcode.com/

## The Puzzles

- [Novice-Level Puzzle](puzzle_1.md): For those who have recently started using Python.
- [Easy Puzzle](puzzle_2.md): For beginners who know their way around the basics.
- [Intermediate Puzzle](puzzle_3.md): A slightly more demanding puzzle for the more fluent Pythonistas.

## Advanced Puzzle: Some Assembly Required

From day 7 of 2015: <https://adventofcode.com/2015/day/7>

#### Part 1

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

#### Part 2

Now, take the signal you got on wire `a`, override wire `b` to that signal, and reset the other wires (including wire `a`). What new signal is ultimately provided to wire `a`?
