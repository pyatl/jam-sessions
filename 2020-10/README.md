# Binary Search

PyATL Jam Session, October 1st 2020

## Part 1: Guess the Number!

*Note: If you are already very familiar with this problem, you may want to go
straight to part 2.*

Let's play a game! Here are the rules:

1. The computer will pick a random number between 1 and 100 (included).
2. Your goal is to find that number, as quickly as possible!
3. When you make a guess, the computer will tell you whether it is correct,
   too low or too high.

You may have seen or done this exercise before; it usually implies writing the
code for the game. But today, we are turning the roles around: I have already
written the game, and your job is to write code that plays it.

### Instructions

In `guess_number.py`, write code that plays the number guessing game. It will
need to figure out the number then stop running. To check if your code works,
click "test" in the upper-left of the screen.

In there, you will see `from mystery_number import guess_number`; don't remove
it! `guess_number` is a function that takes a number as input and that returns
a string indicating how your guess was: either `"too large"`, `"too small"`,
or `"correct"`. For example, if the number was 71:

    guess_number(50)
    "too small"
    guess_number(95)
    "too large"
    guess_number(71)
    "correct"

Note that `guess_number` will pick a different number every run, and always
fail after 100 guesses.

### Tips

The principal idea here is to start in the middle, and progress by steps using
what the computer tells you until the number is found. For example:

1. Start by guessing 50, since that's in the middle between 1 and 100.
   You get back "too large", now you know that the number is between 1 and 49
2. Now, use the new middle of that range as a guess, in this case 25. You get
   back "too small", so the number is between 26 and 49.
3. Pick the middle again. It's (26 + 49) / 2 = 37. The reply is "too large"
   again, so the number is between 26 and 36.
4. Repeat: pick (26 + 36) / 2 = 31. That is "too small", the range is 32-36.
5. Repeat: pick (32 + 36) / 2 = 34. "too small" again, so the number that was
   picked is either 35 or 36. You're almost there!
6. With not many options, try 35. Still "too small", therefore…
7. only one possibility left: 36, and that's "correct"!

At each step of the process, you were able to divide the range of possible
guesses by two. That's why this process is called "binary search".

The main difficulty of the exercise is to get the indices right. It's easy to
forget a ±1 somewhere and have your code loop forever…

If you want more information on binary search and its uses, there are countless
resources online. Here is one recent video by Tom Scott on the topic:
https://youtu.be/KXJSjte_OAI

## Part 2: Pokémon Debugging Symbols Look-Up

In the files `pokeblue_rom00.sym` through `pokeblue_rom03.sym`, you will find
the [community-created][pret-pokered] symbols (names for routines and data in
the code) for the first 64 KiB of the [Pokémon Blue] game on the Game Boy.

Each file corresponds to a 16 KiB segment, also called a "bank". Each line of
those files is composed of an address followed by a name, as such:
    
    01:77c2 PokemonMenuEntries

The address itself is composed of a bank number followed by an offset. Both
values are hexadecimal. The offset is between 0 and 0x3fff for bank 0, and
between 0x4000 and 0x7fff for all other banks.

The lines in each file are ordered by address. There may be more than one
symbol per address.

For this part, write your code in `pokemon_symbols.py`. To 

### Challenge 1

Write a `pokemon_get_symbol` function that takes an address as input and
returns the symbol name at that address if it exists, or `None` otherwise. If
there is more than one symbol that can be returned, pick that last one.

Examples:
   * `pokemon_get_symbol("01:4524")` returns `"LoadTitleMonSprite"`
   * `pokemon_get_symbol("03:5000")` returns `None` (there is no symbol there)
   * `pokemon_get_symbol("03:4503")` returns `"PokecenterWarpTileIDs"`

### Challenge 2

Write a `pokemon_last_symbol` function that acts like the previous one, but
when no symbol exists at the given address it should return the last symbol
*before* that address.

Examples:
   * both `pokemon_last_symbol("02:7c2e")` and `pokemon_last_symbol("02:7c40")`
     return `"Music_SafariZone_Ch1"`
   * `pokemon_last_symbol("03:5000")` returns `"WildDataPointers"`
   * `pokemon_last_symbol("03:4504")` returns `"PokecenterWarpTileIDs"`
   * `pokemon_last_symbol("00:0040")` returns `None` (no last symbol exists)

### Notes

* An understanding of how the addresses work is not actually required. You can
  store them as strings, and the exercise will still work.

* You could solve the first challenge with a dictionary, but that wont' work
  for the second (at least not efficiently). I think binary search works nicely
  in that case, though there may be other good solutions.
  
* Tired of re-writing the binary search code every time you need it? The
  [`bisect` standard library][bisect] can help!

* If you are confused by how the addresses work, here is a short explanation:
  the CPU of the Game Boy only addresses memory over 16 bits, which limits the
  total memory to 64 KiB. Of that, only the first half is mapped to the ROM
  (read-only memory) cartridge. But that's really not a lot… To solve this, the
  second half of the ROM (addresses 0x4000 through 0x7fff) can show any 16 KiB
  block of the ROM; this is called banking. The first 16 KiB (0x0000 through
  0x3fff) are hard-wired to display the first block (bank 0). More info:
  <https://youtu.be/ecTQVa42sJc>


[pret-pokered]: https://github.com/pret/pokered
[Pokémon Blue]: https://en.wikipedia.org/wiki/Pokémon_Red_and_Blue
[bisect]: https://docs.python.org/3/library/bisect.html
