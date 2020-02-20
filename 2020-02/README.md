# PyATL Jam Session – Feb. 6th, 2020

This month's puzzle: **Roman Numerals Converter**

* Cyber-Dojo code: `cf67GH`
* [Link to the dashboard](https://www.cyber-dojo.org/dashboard/show/cf67GH)
* [Link to the document](http://bit.ly/jam-session-2020-02)

Table of contents:
* [Instructions](#instructions)
* [Solutions](#solutions)

## Instructions

Write code in `roman.py` that converts a number (passed as an integer) into its Roman Numeral notation:

https://en.wikipedia.org/wiki/Roman_numerals#%22Standard%22_forms

The Roman numeral notation uses letters to represent multiples of ten and five, the common letters being:

    I =    1
    V =    5
    X =   10
    L =   50
    C =  100
    D =  500
    M = 1000

The multiples of 4 and 9 are generally represented by subtracting one from the next value, e.g.:

    IV ~    5 -   1 =   4
    IX ~   10 -   1 =   9
    XL ~   50 -  10 =  40
    XC ~  100 -  10 =  90
    CD ~  500 - 100 = 400
    CM ~ 1000 - 100 = 900

When representing the numbers from 1 to 10, this looks like:

    I, II, III, IV, V, VI, VII, VIII, IX, X

The input numbers will be between 1 and 3,999 included (the largest value the standard notation can represent).

See the Wikipedia page for details, and a bunch more examples.

### Extras

Here are some extra features you can implement as a challenge:

- Write a Roman to integer decoder, basically the inverse function.
- Make that decoder also work with the variant forms, such as the additive notation (e.g. IIII as 4)
- Add support for the Unicode Roman Numerals

## Solutions

While the Roman numeral notation is somewhat decimal, the principal difficulty resides in how it represents powers of tens of 4 and 9.

My approach (and others did the same) was to reduce the number by steps, starting from the largest symbol ("M") until nothing is left.

For example, here's the process for 2,470:

1. Starting with `M` (1,000), our number is larger so we subtract 1,000 from it(now 1,470) and use `M` as the first letter of our result.
2. The number is still greater than 1,000 so we repeat the process. The number is now 470 and our result `MM`.
3. The next symbols are `CM` (900) and `D` (500) but our number is smaller than both. So we skip those straight to `CD` (400) that we process. The number is now 70 and the result `MMCD`.
4. The next largest symbol is `L` (50) that we can subtract once. We now have 20 left and the result is `MMCDL`.
5. Finally, we subtract `X` (10) from the number twice, giving us `MMCDLXX`. The number left is zero so the process is complete. 

The solution is coded as follows:

```python
ROMAN_NUMBERS = {
    "M": 1000, "CM": 900, "D": 500, "CD": 400,
    "C": 100, "XC": 90, "L": 50, "XL": 40,
    "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1,
}

def print_roman(number):
    """Convert an integer into its Roman numeral representation"""
    if not 0 < number < 4000:
        raise ValueError("Roman numbers only work from 1 to 3,999")

    result = ""
    for roman, num in ROMAN_NUMBERS.items():
        while number >= num:
            result += roman
            number -= num
    return result
```

This relies on a property of Dictionaries in Python 3.6 and up: they are ordered, which means that iterating over the keys will yield them in the same order as they were inserted. If we tried this approach in older versions of Python, we would have to use a list of tuples.

### Alternatives

First, several other people implemented very similar approaches to the one above, in slightly different ways: [hyena] and [whale] in particular. [Skunk]'s approach is a slightly different take, where the ones and fives of each power of ten are counted, and the symbols built on those counts.

I also found [turtle]'s answer interesting because it is basically the same approach as mine,but where the fours and nines are built "logically" without special logic and are replaced at the end using string substitution. It is very pragmatic and I like it.

The other main approach that several of the solutions used is to traverse the number digit by digit (starting with the units digit). This involves keeping track of the position to know which symbols to use.

Below is a mash-up inspired mainly by [rabbit]'s answer but that takes a few other good ideas from other solutions.

```python
ROMAN_CODES = ["IVX", "XLC", "CDM", "M__"]

def print_roman_build_up(number):
    result = ""
    for one, five, ten in ROMAN_CODES:
        number, digit = divmod(number, 10)
        if digit == 9:
            symbol = one + ten
        elif digit == 4:
            symbol = one + five
        else:
            symbol = five * (digit // 5) + one * (digit % 5)
        result = symbol + result
    return result
```

In this solution I used the [divmod] built-in to gradually reduce the number by steps of ten _and_ extract the corresponding digit. I also used string unpacking in the `for` loop to split the codes into symbols.

The other solutions (like [bison]'s and [crab]'s) use a similar approach but with the patterns already defined in advance (where the above solution used arithmetic to build each symbol).

This pattern-based approach allows us to cheat a little by building all the known patterns ahead of time. Here is a solution I built that does that. As a result, it is more than twice as fast as the first solution I showed:

```python
ROMAN_PATTERNS = [
    "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX",
    "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC",
    "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM",
    "", "M", "MM", "MMM",
]

def print_roman(number):
    place, roman_num = 0, ""
    while number:
        roman_num = ROMAN_PATTERNS[place * 10 + number % 10] + roman_num
        number //= 10
        place += 1
    return roman_num
```

[divmod]: https://docs.python.org/3/library/functions.html#divmod

[bison]: https://www.cyber-dojo.org/review/show/9xyjS1?was_index=5&now_index=5&filename=roman.py
[crab]: https://www.cyber-dojo.org/review/show/3frl3E?was_index=9&now_index=9&filename=roman.py
[hyena]: https://www.cyber-dojo.org/review/show/N8HX2a?was_index=4&now_index=4&filename=roman.py
[rabbit]: https://www.cyber-dojo.org/review/show/jWPQqb?was_index=3&now_index=3&filename=roman.py
[skunk]: https://www.cyber-dojo.org/review/show/D9WSbt?was_index=21&now_index=21&filename=roman.py
[turtle]: https://www.cyber-dojo.org/review/show/JjhwmC?was_index=4&now_index=4&filename=roman.py
[whale]: https://www.cyber-dojo.org/review/show/k5F30e?was_index=1&now_index=1&filename=roman.py
