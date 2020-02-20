import unicodedata

# My own solution, the "Salmon" one on cyber-dojo:
# https://www.cyber-dojo.org/review/show/VF8Wub?was_index=9&now_index=9&filename=roman.py

ROMAN_NUMBERS = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
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


# Proposed solution to the extras


def parse_roman(string):
    """Convert a roman number into an integer"""
    # Deal with unicode funk by normalizing it
    # e.g. Normalizing "\u216A" => "XII"
    string = unicodedata.normalize("NFKD", string).upper()

    # Iterate over the pairs of characters
    prev, number = string[0], 0
    for char in string[1:]:
        n_prev, n_char = ROMAN_NUMBERS[prev], ROMAN_NUMBERS[char]

        # If order of value is inverted, the pair should be a 4 or 9
        if n_prev < n_char:
            # The value of the second char will be added at the
            # next step so we need to subtract it to balance that.
            number += ROMAN_NUMBERS[prev + char] - n_char
        else:
            number += n_prev
        prev = char

    # Loop above does not include last char, deal with it here
    number += ROMAN_NUMBERS[prev]
    return number


# Alternative solutions below


def print_roman_turtle(number):
    # Translate then replace, adapted from "Turtle's" approach
    # https://www.cyber-dojo.org/review/show/JjhwmC?was_index=4&now_index=4&filename=roman.py

    roman_list = ["M", "D", "C", "L", "X", "V", "I"]
    number_list = [1000, 500, 100, 50, 10, 5, 1]
    quotient_list = []
    roman_string = ""
    count = 0

    for i in number_list:
        if number >= i:
            quotient_list.append(number // i)
            number = number % i
        else:
            quotient_list.append(0)

    while count < len(number_list):
        roman_string += quotient_list[count] * roman_list[count]
        count += 1

    roman_string = roman_string.replace("DCCCC", "CM")
    roman_string = roman_string.replace("CCCC", "CD")
    roman_string = roman_string.replace("LXXXX", "XC")
    roman_string = roman_string.replace("XXXX", "XL")
    roman_string = roman_string.replace("VIIII", "IX")
    roman_string = roman_string.replace("IIII", "IV")
    return roman_string


def print_roman_bison(number):
    # Pattern-based approach, adapted from "Bison's" answer
    # https://www.cyber-dojo.org/review/show/9xyjS1?was_index=5&now_index=5&filename=roman.py

    # Here are the roman numerals, in order
    roman_list = ["I", "V", "X", "L", "C", "D", "M"]

    # note that the pattern of symbols repeats for the 1's, 10's, 100's column
    # this means we only need 10 patterns, and can replace the symbols
    # depending on whether we're concerned with 1's, 10's, etc
    pattern_dict = {
        "1": "x",
        "2": "xx",
        "3": "xxx",
        "4": "xy",
        "5": "y",
        "6": "yx",
        "7": "yxx",
        "8": "yxxx",
        "9": "xz",
        "0": "",
    }

    # the index in our symbol list; determines if we are doing 1's, 10's, etc
    places = 0

    # initialize blank string
    roman_num = ""

    # go digit by digit, starting with 1's
    for x in str(number)[::-1]:
        # based on the digit, pick the pattern. then replace x,y,z with
        # appropriate symbols based on which column we're in
        pattern = pattern_dict[x]
        if places < 6:
            pattern = pattern.replace("x", roman_list[0 + places])
            pattern = pattern.replace("y", roman_list[1 + places])
            pattern = pattern.replace("z", roman_list[2 + places])
        else:
            pattern = pattern.replace("x", roman_list[0 + places])

        # prepend our pattern to the string we're building
        roman_num = pattern + roman_num
        # advance to the next column's symbols
        places = places + 2

    return roman_num


def print_roman_rabbit(number):
    # Position-encoding approach, based on "Rabbit's" answer:
    # https://www.cyber-dojo.org/review/show/jWPQqb?was_index=3&now_index=3&filename=roman.py

    codes = ["IVX", "XLC", "CDM", "M-+"]

    def encode_single(_num, _i):
        code = codes[_i]
        _out = ""
        if _num >= 9:
            _out += code[2]
        elif _num >= 4:
            _out += code[1]
        if _num % 5 == 4:
            return code[0] + _out
        else:
            return _out + code[0] * (_num % 5)

    out = ""
    nums = str(number)
    for i, num in enumerate(nums[::-1]):
        out = encode_single(int(num), i) + out
    return out


def print_roman_crab(number):
    # Explicit rules replacement, based on "Crab's" answer
    # https://www.cyber-dojo.org/review/show/3frl3E?was_index=9&now_index=9&filename=roman.py

    # Each "digit" of a Roman numeral is built by the following pattern:

    # For every power of 10 'e':
    # 1e = one
    # 2e = one + one
    # 3e = one + one + one
    # 4e = one + five
    # 5e = five
    # 6e = five + one
    # 7e = five + one + one
    # 8e = five + one + one + one
    # 9e = one + ten

    # To build the full numeral, iterate over the digits of the integer passed in.
    # Build each digit as a string, then append that string to the finished numeral.

    roman_numeral_digits = [
        "I",  # 1
        "V",  # 5
        "X",  # 10
        "L",  # 50
        "C",  # 100
        "D",  # 500
        "M",  # 1000
    ]

    # Notice that in the above array, the powers of 10 'e' are at array position
    # 2 * e, such that the 'one' value is at [2*e], the 'five' value is at [2*e+1],
    # and the 'ten' value is at [2*e+2]

    # The current power of ten. We start in the ones place (10^0).
    e = 0

    # The numeral string we're building.
    numeral = ""

    # At the end of each loop, the number will be integer-divided by 10. This will
    # eventually drop the number to 0 and end the loop.

    while number > 0:
        current_digit = number % 10

        try:
            one = roman_numeral_digits[2 * e]
        except IndexError:
            one = ""

        try:
            five = roman_numeral_digits[2 * e + 1]
        except IndexError:
            five = ""

        try:
            ten = roman_numeral_digits[2 * e + 2]
        except IndexError:
            ten = ""

        roman_numeral_rules = {
            0: "",
            1: one,
            2: one + one,
            3: one + one + one,
            4: one + five,
            5: five,
            6: five + one,
            7: five + one + one,
            8: five + one + one + one,
            9: one + ten,
        }

        # Put each new digit at the left side of the string.
        numeral = roman_numeral_rules[current_digit] + numeral

        # Divide the number by 10 to continue the march through its digits.
        number = number // 10

        # In the next loop we'll work on the next highest power of 10.
        e += 1

    return numeral


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


_ROMAN_PATTERNS = [
    "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX",
    "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC",
    "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM",
    "", "M", "MM", "MMM",
]


def print_roman_fastest(number):
    # "Dirty" approach heavily inspired by bison's. But this one is FAST.
    place, roman_num = 0, ""
    while number:
        roman_num = _ROMAN_PATTERNS[place * 10 + number % 10] + roman_num
        number //= 10
        place += 1
    return roman_num
