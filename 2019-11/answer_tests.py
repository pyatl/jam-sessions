"""
Whoops, wrong way! This file contains the magic used to verify your
puzzle answers without giving the solutions (immediately) away.

For best puzzle enjoyment, please do not edit this.
"""
import importlib
import pytest

# This contains the answers! Hidden so you can't cheat too easily!
# Look, I'm not your parent; reverse-engineer this if you want.
# It's just a pickled dictionary, nothing too fancy.
SECRET = (
    b'gASVrgAAAAAAAAB9lCiMD3B1enpsZV8xLnBhcnRfMZRL6IwPcHV6emxlXzEucG'
    b'FydF8ylE33BowPcHV6emxlXzIucGFydF8xlEp8NBgAjA9wdXp6bGVfMi5wYXJ0'
    b'XzKUSpoHOQCMD3B1enpsZV8zLnBhcnRfMZRL7IwPcHV6emxlXzMucGFydF8ylE'
    b'szjA9wdXp6bGVfNC5wYXJ0XzGUTfGzjA9wdXp6bGVfNC5wYXJ0XzKUTTY3dS4='
)

def _decode_answers(secret: bytes):
    import pickle, base64
    return pickle.loads(base64.b64decode(secret))

# This is a dictionary of puzzle functions to load as keys
# (e.g. "puzzle_1.part_1"), with the answers as values.
__ANSWERS = _decode_answers(SECRET)

@pytest.fixture(params=list(__ANSWERS))
def puzzle_data(request):
    mod_name, func_name = request.param.split('.')

    module = importlib.import_module(mod_name)
    function = module.__dict__[func_name]

    with open(f"{mod_name}.txt") as f:
        data = f.read().strip().splitlines()
        if len(data) == 1:
            data, = data

    return function, data, __ANSWERS[request.param]

def test_puzzle(puzzle_data):
    function, data, answer = puzzle_data

    res = function(data)
    if res is NotImplemented:
        pytest.skip("Not solved yet")

    if res != answer:
        pytest.fail(f"BZZZT! {res} is the wrong answer", pytrace=False)
