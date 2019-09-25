# LSB Steganography

PyATL Jam Session — Oct. 3rd, 2019

From an original idea by [@Burnsedia](https://github.com/Burnsedia)

#### Contents

- [Instructions](#instructions)
- [Introduction](#introduction)
- [Part 1: LSB Manipulation](#part-1-lsb-manipulation)
- [Part 2: Reading a Message](#part-2-reading-a-message)
- [Part 3: Writing messages](#part-3-writing-messages)
- [Extra Challenges](#extra-challenges)

## Instructions


First, join the online Cyber-Dojo session:

1. Go to <https://www.cyber-dojo.org/>
2. Select "We're in a group", then "Join a session"
3. Enter the ID that will be shared with the group at the time of the meeting, or on the Meetup page directly.
4. An animal will be assigned to you, then you will be able to start coding on the next page.

On the Cyber-dojo interface, you will see:

* The editor (middle / bottom-right), which occupies most of the page and is where you will be coding.
* The list of files (on the left):
  * `my_code.py` is where you should write your code, and contains a very bare stub of functions at the start.
  * `test_my_code.py` contains the tests that will be run on your code.
* Your test run history (top bar of the page), which will be empty to start with. Tests are color-coded as:
  * green: all tests passed
  * red: at least one test failed
  * yellow: there was an unexpected error while running the tests

To try your code, click the "Test" button at the top-left. This will run the tests in `test_my_code.py` on the code in `my_code.py`.

To add a test, just add a new function in `test_my_code.py`. The only rule is that the function name must start with `test_`. In the function itself, write your tests using `assert` with anything that evaluates to `True` or `False` behind. For example:

```python
def test_something():
    assert 1 == 1
```

If you feel stuck, you can add `print()` calls in your code to see what's going on. Don't hesitate to ask for help!

## Introduction

[Steganography] is the process of hiding one message inside another. You've probably done something like that when you were younger, for example by having the first letter of every sentence in a text form a sentence of its own.

In today's challenge, we will play around with one of the many modern steganography methods: Least Significant Bit (LSB) encoding. This technique allows one to hide a message (or an image) in another document where very tiny changes won't be noticeable, such as a picture or music.

For the sake of keeping the exercise simple, we sadly won't be manipulating images but just simple text. But armed with your knowledge and code, you can explore doing that if your curiosity calls for it!

## Part 1: LSB Manipulation

First, let's study some fundamental principles. In most digital applications, the unit of data is called a [Byte], which holds 8 bits of data. Consequently, a byte has 2⁸ = 256 possible states, usually represented as a number between 0 and 255. For example:

    71 (dec) = 0 1 0 0 0 1 1 1 (bin)

The binary code for a byte is read from left to right with decreasing powers of two: 128, 64, 32, 16, 8, 4, 2, and 1:

    Bits:     0  1  0  0  0  1  1  1
    Weight: 128 64 32 16  8  4  2  1
    Sum:      0 64  0  0  0  4  2  1  = 71

In this case, 71 = 64 + 4 + 2 + 1. Interestingly, our decimal system works the same way, i.e. 71 = 7 × 10 + 1 × 1.

In that binary representation, the bit furthest to the right is called the _least significant bit_ (LSB), because changing it impacts the value the least. Conversely, the bit on the left is the _most significant bit_, since changing it impacts the value the most:

    0 1 0 0 0 1 1 0 (bin) = 70 (dec)
    0 1 0 0 0 1 1 1 (bin) = 71 (dec)
    1 1 0 0 0 1 1 1 (bin) = 199 (dec)


**Exercise 1:** Write code that can extract the LSB from a number. You can assume that the number you will be given is always positive.

Examples:

* The LSB of 0 is 0
* The LSB of 1 is 1
* The LSB of 71 is 1

**Exercise 2:** Write code to replace the LSB of a number by a given value.

Examples:

* Replacing the LSB of 0 or 1 by 0 yields 0
* Replacing the LSB of 71 by 0 yields 70
* Replacing the LSB of 212 by 1 yields 213

**Exercise 3:** Write code that returns the bits of a byte, from most significant to least significant. Always return 8 bits. You can assume that your input is always between 0 and 255.

Examples:

* The bits of 0 are `[0, 0, 0, 0, 0, 0 ,0 ,0]`
* The bits of 32 are `[0, 0, 1, 0, 0, 0, 0, 0]`
* The bits of 212 are `[1, 1, 0, 1, 0, 1, 0, 0]`

**Exercise 4:** Write code that does the reverse of the code above, i.e. from a list of 8 bits it returns the corresponding value.

#### Tips

* Write each exercise as its own function with a meaningful name, you will need those later.

* You can do exercises 3 and 4 first and use their code to solve 1 and 2, but always splitting a number into all its bits is not the most efficient way of manipulating the LSB only.

* Have you noticed that the LSB of a number basically dictates whether a number is odd or even? You may want to try playing with the Modulo (`%`) and Integral Division (`//`) operations in Python! 

* Alternatively, Python has some [Bitwise Operators] you can try to use.

* You can also use the `bin` builtin to display the binary value of any number:
    ```
    >>> bin(71)
    '0b1000111'
    ```
  Be warned that it does not always return 8 bits, only as many as needed. If you do use `bin` to solve exercise 3, be careful about returning the correct data type (integers and not digits as strings).

## Part 2: Reading a Message

Now that we know how to manipulate bits and bytes, let's put that knowledge to use to read messages. This is done in three steps:

1. Given a list (or stream) of bytes, extract the LSB of each.
2. Group those bits by clusters of eight. Remaining bits (fewer than 8 at the end) are discarded.
3. Convert each cluster of 8 to a byte, and output those values.

**Exercise 5:** Write code that does just that!

Example: This sequence of 8 bytes contains the number 88

    72, 187, 42, 73, 41, 94, 50, 66

**Challenge 1:** What numbers are hidden in this sequence?

    88, 249, 116, 150, 121, 220, 62, 144, 80, 19, 3, 228, 180, 145, 92, 235,
    50, 141, 27, 18, 145, 25, 110, 198, 0, 83, 253, 228, 201, 245, 202, 78,
    180, 41, 205, 60, 83, 83, 229, 201, 90, 56, 13, 112, 36, 72, 130, 187

Numbers are fun, but they're not much use to us… yet. To get text, there are two steps to apply.

1. Convert your stream of numbers into a byte-string. This is pretty straightforward:
   ```
   >>> bytes([80, 121, 116, 104, 111, 110])
   b'Python'
   ```
2. Convert the byte-string into a string using the `bytes.decode()` method. This step is important if the message originally contained funky characters:
   ```
   >>> b'Python'.decode()
   'Python'
   >>> b'4 \xc3\x97 5 \xc3\xb7 2 = 10'.decode()
   '4 × 5 ÷ 2 = 10'
   ```

**Exercise 5:** Make your stenography reader print the hidden messages! What was the message hidden in the numbers of challenge 1?

Conversely, a byte-string can be iterated over and will yield integers:

    >>> list('Python')
    ['P', 'y', 't', 'h', 'o', 'n']
    >>> list(b'Python')
    [80, 121, 116, 104, 111, 110]

This means that we can take a byte-string in and extract a message from it.

**Exercise 6:** Make your code work if passed `bytes` instead of a list of numbers.

**Challenge 2:** What's the message hidden in here?

    @ehpirbhng!bhcdodum est tmurichdr!inueger qthr atbunr dliu!sdd.
    Udlmus!au tsn` condhmdoutl!l`tthr qdlldntdsptd hd.!Vdl pt`m dldldnutl ptlvin`r dthal nnn pu`l.

**Challenge 3:** And in this one?

    Losdm hprum!dolnr!sit!`ldu-!bnnrdcuetts!`diqirchnf!dmiu-
    red!eo!diusmnd!tempos!inciehetot!uu m`bnse!du enlore!m`foa `lipta/
    Du mhfula!umlambnspdr!laldru`ea!psoin mibern ouob!conrequ`t/
    Ab!tiocheunt!witad!sdlpds!pths!lebutr otlm`.
    Pthr!dldhfdne pt`l `ehphrbhng vht`d.

#### Tips

Know the difference between `str` and `bytes`! They look very similar and have almost identical features, which can lead to confusion. They are however fundamentally different, especially when special characters are involved:

* A string (`str`) is text as humans understand it. A unit of text is (almost) always a character.

* A byte-string (`bytes`) is a readable representation of binary data as your computer understands it. It so happens that the ASCII symbols (basic letters and numbers) correspond to some of those values. Anything else is displayed with its hexadecimal value, e.g. `\xc3`. A unit of a byte-string is always a byte. In Python, a byte-string is written like a string but with `b` in front, and may not contain any non-ASCII character.
  
Converting from `str` to `bytes` required _encoding_. The most flexible and popular is UTF-8, which is the default in Python:

    >>> '4 × 5 ÷ 2 = 10'.encode()
    b'4 \xc3\x97 5 \xc3\xb7 2 = 10'

The reverse operation is called _decoding_, which we've already seen in action. Be aware that decoding can easily fail if the binary data is invalid.

When copying the challenge messages, be careful to keep the line jumps and not add any more spaces or newline at the start. Any extra or missing character completely skews the bytes alignment. And don't forget to write them as byte-strings with `b` in front.

## Part 3: Writing messages

From this point onwards, the challenge is more free-form. There won't be as many examples to guide you, so use your judgment accordingly.

Writing Steganography is simply the reverse process of reading. You take two streams of bytes in, one is the message and the other is the carrier data. For each bit of the message, one byte of the carrier is modified and outputted.

**Exercise 7:** Write code to insert a message into another

The interesting challenge here is that there is no guarantee that the carrier will be of exactly the right length to hold the message. You will need to make decisions regarding:

1. What if the carrier is too short? Do you truncate the message or throw an error?
2. What if it is too long? Do you pad the message with spaces? Or do you terminate the message with a null `\x00` byte and leave the carrier unaltered?

## Extra challenges

These are some additional challenges for you to take on freely.

* I've been suggesting to use lists of numbers the entire time, for simplicity. This isn't ideal or efficient for large amounts of data. Can you re-write your code to work lazily, and only output/consume bytes one at a time? You might want to look into using `yield`, `yield from`, and the `itertools` library.

* In the same line of thinking, can you make your code work on other forms of binary data, such as `io.BytesIO`?

* As you can see, doing LSB Steganography on text is a terrible idea because it massively alters the original data (and there is no good way around it; all vowels have the same parity in ASCII!). Doing Steganography on images or music is much more interesting because LSB changes are so small that they usually cannot be detected by humans. Can you apply your code to an image or sound? You will need to work locally for that, as cyber-dojo.org does not provide support for third-party libraries or other types of media.

* Plain binary text is pretty easy to detect. Can you modify your steganography to automatically apply some scrambling or encryption?

[Bitwise Operators]: https://wiki.python.org/moin/BitwiseOperators
[Byte]: https://en.wikipedia.org/wiki/Byte
[Steganography]: https://en.wikipedia.org/wiki/Steganography