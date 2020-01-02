# This file contains the magic that checks if your answers are correct.
# You do not need to edit or understand this code to solve the problem.

from hashlib import md5
import importlib
import pytest

ANSWERS = {
    ("puzzle_1", "part_1"): "adb92f740c067c6366b05e108675c716",
    ("puzzle_1", "part_2"): "7e095a67806e004ff8fac12606804e5a",
    ("puzzle_2", "part_1"): "d7b039cb4722ed2736a90273a9c4ead7",
    ("puzzle_2", "part_2"): "094bb65ef46d3eb4be0a87877ec333eb",
}

@pytest.mark.parametrize("puzzle,part", list(ANSWERS))
def test_puzzle(puzzle, part):

    module = importlib.import_module(puzzle)
    function = module.__dict__[part]
    with open(f"{puzzle}.txt") as file:
        data = file.read()

    result = function(data)
    if result is NotImplemented:
        pytest.skip("Not solved yet")

    result_hash = md5(str(result).encode()).hexdigest()
    if result_hash != ANSWERS[(puzzle, part)]:
        pytest.fail(f"BZZZT! {result} is the wrong answer", pytrace=False)
