# Novice Puzzle: Not Quite Lisp

From Advent of Code 2015, Day 1: <https://adventofcode.com/2015/day/1>

Write your code in `puzzle_1.py`. The functions `part_1` and `part_2` will automatically be provided with the puzzle input from `puzzle_1.txt`, as a string.

### Part 1

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

### Part 2

Now, given the same instructions, find the **position** of the first character that causes him to enter the basement (floor `-1`). The first character in the instructions has position `1`, the second character has position `2`, and so on.

For example:

- `)` causes him to enter the basement at character position `1`.
- `()())` causes him to enter the basement at character position `5`.

What is the **position** of the character that causes Santa to first enter the basement?

### Tips

* Here's more explanations on how solving the puzzle works. In `puzzle_1.py`, you will find two functions `part_1` and `part_2` that don't do anything — for now.  
  Your work is to fill in those functions with code that solves the respective parts of the problem. For example, `part_1("(())")` is expected to return 0.  
  The full input your code needs to handle is in `puzzle_1.txt`. You don't need to worry about reading the file, the automated tests will do that for you and pass its contents as the `directions` argument.

* This is a great opportunity to use a `for` loop! In Python, you can use it on strings
to iterate over its characters:

    ```python
    >>> for letter in "Hello!":
    ...     print(letter)
    H
    e
    l
    l
    o
    !
    ```

* When an exercise gives you examples, it's a good idea to implement those as unit tests so that you can check if you code works. In `test_puzzles.py`, you can add:

    ```python
    import puzzle_1
  
    def test_puzzle1_part1():
        assert puzzle_1.part_1('(())') == 0
        assert puzzle_1.part_1('(()(()(') == 3
        assert puzzle_1.part_1(')())())') == -3
    ```