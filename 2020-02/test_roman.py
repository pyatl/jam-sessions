import unicodedata

import pytest

from roman import *


# The print_roman function from roman.py will be run once for
# each tuple in this list. The number on the right will be passed
# as argument, and we test that the output is equal to the roman
# number on the left.
TESTS = [
    # 1-10
    ("I", 1),
    ("II", 2),
    ("III", 3),
    ("IV", 4),
    ("V", 5),
    ("VI", 6),
    ("VII", 7),
    ("VIII", 8),
    ("IX", 9),
    # 10-100
    ("X", 10),
    ("XX", 20),
    ("XXX", 30),
    ("XL", 40),
    ("L", 50),
    ("LX", 60),
    ("LXX", 70),
    ("LXXX", 80),
    ("XC", 90),
    # 100-1000
    ("C", 100),
    ("CC", 200),
    ("CCC", 300),
    ("CD", 400),
    ("D", 500),
    ("DC", 600),
    ("DCC", 700),
    ("DCCC", 800),
    ("CM", 900),
    # 1000-3000
    ("M", 1000),
    ("MM", 2000),
    ("MMM", 3000),
    # Decimal places examples
    ("XXXIX", 39),
    ("CCXLVI", 246),
    ("DCCLXXXIX", 789),
    ("MMCDXXI", 2421),
    # Missing places
    ("CLX", 160),
    ("CCVII", 207),
    ("MIX", 1009),
    ("MLXVI", 1066),
    # Large numbers
    ("MDCCLXXVI", 1776),
    ("MCMLIV", 1954),
    ("MMXIV", 2014),
    ("MMXX", 2020),
]

APPROACHES = [
    print_roman,
    print_roman_rabbit,
    print_roman_bison,
    print_roman_turtle,
    print_roman_crab,
    print_roman_skunk,
    print_roman_build_up,
    print_roman_fastest,
]


@pytest.mark.parametrize("parse_function", APPROACHES)
@pytest.mark.parametrize("roman_num,integer", TESTS)
def test_print_roman(parse_function, roman_num, integer):
    assert parse_function(integer) == roman_num


@pytest.mark.parametrize("roman_num,integer", TESTS)
def test_parse_roman(roman_num, integer):
    assert parse_roman(roman_num) == integer


ROMAN_UNICODE = [chr(0x2160 + n) for n in range(32)]


@pytest.mark.parametrize("roman_char", ROMAN_UNICODE)
def test_parse_unicode(roman_char):
    value = int(unicodedata.numeric(roman_char))
    assert parse_roman(roman_char) == value
