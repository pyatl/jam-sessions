
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

## Novice Puzzle: Not Quite Lisp

From day 1 of 2015: <https://adventofcode.com/2015/day/1>

Input for this puzzle is provided in the Cyber-Dojo session in `day_01.txt`.

#### Part 1

Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor `0`) and then follows the instructions one character at a time.

An opening parenthesis, `(`, means he should go up one floor, and a closing parenthesis, `)`, means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

- `(())` and `()()` both result in floor `0`.
- `(((` and `(()(()(` both result in floor `3`.
- `))(((((` also results in floor `3`.
- `())` and `))(` both result in floor `-1` (the first basement level).
- `)))` and `)())())` both result in floor `-3`.

To **what floor** do the instructions take Santa?

#### Part 2

Now, given the same instructions, find the **position** of the first character that causes him to enter the basement (floor `-1`). The first character in the instructions has position `1`, the second character has position `2`, and so on.

For example:

- `)` causes him to enter the basement at character position `1`.
- `()())` causes him to enter the basement at character position `5`.

What is the **position** of the character that causes Santa to first enter the basement?

## Easy Puzzle: I Was Told There Would Be No Math

From day 2 of 2015: <https://adventofcode.com/2015/day/2>

#### Part 1

The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length `l`, width `w`, and height `h`) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect [right rectangular prism](https://en.wikipedia.org/wiki/Cuboid#Rectangular_cuboid)), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is `2*l*w + 2*w*h + 2*h*l`. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

- A present with dimensions `2x3x4` requires `2*6 + 2*12 + 2*8 = 52` square feet of wrapping paper plus `6` square feet of slack, for a total of `58` square feet.
- A present with dimensions `1x1x10` requires `2*1 + 2*10 + 2*10 = 42` square feet of wrapping paper plus 1 square foot of slack, for a total of `43` square feet.

All numbers in the elves' list are in feet. How many total **square feet of wrapping paper** should they order?

#### Part 2

The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

- A present with dimensions `2x3x4` requires `2+2+3+3 = 10` feet of ribbon to wrap the present plus `2*3*4 = 24` feet of ribbon for the bow, for a total of `34` feet.
- A present with dimensions `1x1x10` requires `1+1+1+1 = 4` feet of ribbon to wrap the present plus `1*1*10 = 10` feet of ribbon for the bow, for a total of `14` feet.

How many total **feet of ribbon** should they order?