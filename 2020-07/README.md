# Run-Length Encoding

PyATL Jam Session, July 2nd 2020

---

For this month's Jam, we will be playing around with a relatively simple compression algorithm called [Run-Length Encoding] (RLE).

This exercise is divided in three parts of increasing difficulty:
* The [first part](#part-1-basic-implementation) should be accessible to beginners, so give it a try!
* The [second part](#part-2-handling-strings-with-numbers) should still be relatively easy, for when you're done with part 1.
* [Part three](#part-3-packets-for-the-lone-characters) will be more challenging!

This exercise was inspired by the [Pokémon Sprite Decompression Explained] video from the Retro Game Mechanics Explained Youtube channel.

[Run-Length Encoding]: https://en.wikipedia.org/wiki/Run-length_encoding

## Part 1: Basic Implementation

_Note:_ There are some [Tips and Tricks](#tips-and-tricks) at the end of the document if you need help with the Python code.

The basic idea of RLE is to summarize many consecutive symbols by counting the length of that sequence. Here are a few examples:

- The string `'AAAAAAAA'` is the letter A eight times, so it's compressed as `'8A'`.
- The string `'AAAAABBB'` has A five times followed by B three times, so it's compressed as `'5A3B'`.
- The string `'AAAABBAA'` has two separate groups of As, so we need to group them separately: `'4A2B2A'`
- The string `'AAAACBBB'` has a lone C between two other groups, but our rule of counting still applies so we compress this as `'4A1C3B'`.

More examples:

- `'ABCD'` becomes `'1A1B1C1D'`
- `'AAAAAAAAAAAAAAAAAAAA'` becomes `'20A'`
- `'AAAAZZGGGYYYYYYYYYBCEEEE'` becomes `'4A2Z3G9Y1B1C4E'`

[Video example][rgme-1] (up to 6:36)

**Exercise 1:** Write code that can compress a string of letters as showed above.

**Exercise 2:** Write code that can do the reverse operation, which means transforming the compressed string back into its full form.

## Part 2: Handling Strings With Numbers

The algorithm we implemented in part 1 has a big flaw: it cannot safely compress strings with numbers in them. For example, `'111122222222222'` has four 1s and eleven 2s so it would be compressed `'41112'`. But that's ambiguous: is this `4 x '1' + 10 x '2'`, `41 x '1' + 1 x '2'`, or `4112 x '2'`?

We can solve this by limiting the size of any group to 9. If a sequence is longer than 9, we split it in groups of fewer than 9 as many times as needed.

In the example above, `'111122222222222'` would become `'419222'`, which can only represent `4 x '1' + 9 x '2' + 2 x '2'`. There are other valid options such as `414272`, but it's easiest to group by up to 9 from the left.

A few examples:

- `'77777777777777777777777777'` (twenty-six 7s) becomes `'979787'`
- `'222111111111100'` (three 2s, ten 1s, two 0s) becomes `'32911120'`
- `'555555555555555555444444444444444` (eighteen 5s, fifteen 4s) becomes `'95959464'`

All the short examples from part 1 (except the `'20A'` one) should also still work the same.

[Video example][rgme-2] (up to 6:50)

**Exercise 3:** Write code that can compress and decompress any string of letters and numbers in that way.

You can write that code separately, or improve your code from part 1.

## Part 3: Packets for the Lone Characters

While the algorithm we implemented in part 2 is safe, there are cases where it's really not optimal. For example, `'12345'` becomes `'1112131415'` which is twice as long! This is not exactly great when our goal is to compress data.

There's a way to improve this, by making our code have two modes: the RLE mode and the data mode. The RLE mode works as previously, and the data mode stores a sequence of characters un-modified, hopefully saving space compared to RLE.

The trick is in how we indicate whether RLE or data applies. For this, we split our compressed string into "packets", and each packet starts with some way to indicate its mode. There are many ways to implement this, but let's focus on one.

- Our RLE packets will be of the form `'0NV'`. They are always three characters long and start with a zero. The third character `V` is the one being repeated, and the second character `N` is how many times. For example, `'047'` decompresses into `'7777'`.

- Our data packets will be of the form `'NXXX…'` where `N` is the length of the sequence being reproduced, and `'XXX…'` is a sequence of length `N` to be copied as-is. For example, `'43214'` decompresses into `'3214'`.

Because RLE packets always start with `0` and data packets cannot (a data sequence as always a length of at least 1), the algorithm can always tell of what kind the following packet is. And since we also know its length, we can also reliably tell when the next packet starts.

Here is a detailed example; let's decompress `'0412210543040'`:

- Starting from the left, the first thing we see is `0`. So this is an RLE packet made of the first three digits `'041'`, and it decompresses into `'1111'`.
- After this, we are three digits into the string and what's left to decompress is `'2210543040'`.
- The next digit is `2`, so this is a data packet with a payload of length two. Including the length digit, that makes our packet three digits long: `'221'`. It decompresses into `'21'` and we are left with `'0543040'`.
- Next digit is `0`, so this is an RLE packet again: `'054'` decompresses into `'44444'` and leaves `'3040'`.
- Next digit is `3`, so this is again a data packet this time of length three: `'3040'` decompresses into `'040'` and leaves us at the end of the string.

Here is the compressed string visualized with the packet boundaries: `041,221,054,3040`

The final decompressed string is: `'11112144444040'`. With the previous methods it would have been compressed `41121154101410` which is one character longer than this new method.

[This video probably explains it better][rgme-3] (up to 8:35)

Here are some more examples:

- `'0773853'` decompresses into `'7777777853'` (packets: `'077,3853'`)
- `'4234408504317'` decompresses into `'23445555555533337'` (packets: `'42344,085,043,17'`)
- `'030053216058'` decompresses into `'000333331688888'` (packets: `'030,053,216,058'`)
- `'9141026013252'` decompresses into `'14102601352'` (packets: `'9141026013,252'`)
- `'1807303209646964` decompresses into `'833333332226666666666964'` (packets: `'18,073,032,096,46964'`)
- `'0372230950253674068'` decompresses into `'7772355555555555674888888'` (packets: `'037,223,095,025,3674,068'`)

**Exercise 4:** Write code that's able to decompress this form of packet-based RLE

If you're feeling courageous, you can also try write a compressor for this code. There is more than one way to do it, and doing it optimally (the most compressed possible) is challenging! How optimal can you make your compressor? 

## Tips and Tricks

It's easiest to work exclusively with strings, even though the problems from part 2 and part 3 operate on digits. In your code, it should look like:
- Wrong: `my_string = 12345`
- Correct: `my_string = '12345'`
- Also correct: `my_string = "12345"`

Iterating over a string will yield its characters one by one. For example:
- `list('hello')` is `['h', 'e', 'l', 'l', 'o']`
- `for c in 'hello': print(c)` will print each letter of "hello" on a separate line
- `len('hello')` will return its length, 5 in this case

You can build strings by combining them together with `+`:
- `'hel' + 'lo'` is `'hello'`
- It only works with string: `'123' + 123` crashes because you cannot add strings and numbers. You can solve this by converting the number to string: `'123' + str(123)` works.
- `s += ' world!'` will add the given string at the end of `s`. If `s = 'hello'` before that, then `s` will be `hello world!`.

## More Challenges

In the video that inspired this exercise, the Run-Length Encoding explanation is just the beginning… The rest of the video shows RLE being applied to binary data in a very minimalistic way. As a (challenging) exercise, you could try to implement the compression algorithm from the Pokémon game yourself!

See the full video on YouTube: [Pokémon Sprite Decompression Explained]

[rgme-1]: https://youtu.be/aF1Yw_wu2cM?t=365
[rgme-2]: https://youtu.be/aF1Yw_wu2cM?t=396
[rgme-3]: https://youtu.be/aF1Yw_wu2cM?t=410
[Pokémon Sprite Decompression Explained]: https://youtu.be/aF1Yw_wu2cM