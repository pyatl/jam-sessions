# PyATL Jam Session - Mar. 5th, 2020

This month's challenge: **UTF-16 Decoder**

Table of contents:
* [Instructions](#instructions)
* [Part 1](#part-1-reading-code-points)
* [Part 2](#part-2-dealing-with-large-code-points)
* [Part 3](#part-3-combining-pairs-of-bytes)
* [Part 4](#part-4-dealing-with-actual-binary-data)
* [Part 5](#part-5-dealing-with-byte-order)
* [Extra challenges](#extras)
* Bonus: [Explanations](#explanations)
  * [What is Unicode?](#what-is-unicode)
  * [What is an encoding?](#what-is-an-encoding)
  * [Working with Unicode in Python](#working-with-unicode-in-python)

## Instructions

**Overview:** Write code in `utf16.py` that transforms UTF-16 binary data into a string.

If you do not know what [UTF-16] is, don't panic! The problem is split into parts of increasing difficulty, with the first parts accessible to beginners. Each part comes with a list of tips if you are stuck.

_Note:_ That tool already exists as `str.decode()`, the purpose of today's challenge is to (partially) replicate its behavior.

## Part 1: Reading code points

Write code that converts a list of [code points](#what-is-unicode) (numbers) into a string.

### Example:

`[72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]` becomes `"Hello, World!"`.

### Test:

What are the strings behind:

* `[80, 121, 65, 84, 76, 32, 74, 97, 109]`
* `[40, 9583, 176, 9633, 176, 41, 9583, 65077, 32, 9531, 9473, 9531]`
* `[65, 84, 76, 32, 9829, 32, 80, 121, 116, 104, 111, 110, 33, 32, 128013]`

Note: Some of these examples include emoji; they may not display correctly on your browser.

### Tips:

* Convert a code point into its corresponding character with the `chr()` built-in function. For example `chr(97)` is `"a"`.
* Assemble a sequence of characters into a string with `"".join()`. Or you can start with an empty string and a character to it with`+=`.

## Part 2: Dealing with large code points

In the examples above we used the code point 128,013. This code point is considered large because it is bigger than 65,535. The decoding technique we are building here is limited to processing numbers between 0 and 65,535 so how can we make those larger codes work?

This is where **surrogate codes** come in. All code points from 55,296 to 57,343 (included) are reserved for those and cannot be assigned to any character. Their use is designed so that pairs of surrogate numbers can be converted into code points.

To convert a pair of "surrogate" numbers into a code point, where `first` and `second` are the surrogate codes in the order you read them:

    code_point = 65536 + (first % 1024) * 1024 + second % 1024

_Note:_ The `%` operator is called "modulo". It returns what's left when dividing the first number by the second. For example, `17 % 5` is `2` since `17 == 3 * 5 + 2`.

Can you modify your code to decode surrogate pairs before converting the codes into a string?

### Examples:

* The pair of codes `[55296, 56644]` can be decoded as:

        65536 + (55296 % 1024) * 1024 + 56644 % 1024
      = 65536 + 0 * 1024              + 324
      = 65860

  which is the code point for the ancient Greek symbol "fifty" (&#65860;).

* The pair of codes `[55356, 57173]` can be decoded as:

        65536 + (55356 & 1024) * 1024 + 57173 % 1024
      = 65536 + 60 * 1024             + 853
      = 127829

  which is the code point for the "Pizza" emoji (&#127829;).

* In a full string of codes, this would look like:

      [80, 105, 122, 122, 97, 32, 55356, 57173, 32, 76, 97, 110, 100]
  
  This is the string "Pizza &#127829; Land". In this example, there are two surrogate points in the middle that correspond to the previous example. They are converted into the corresponding code point, and all other codes are left as-is. 

### Tests:

What are the strings behind:
* `[80, 121, 116, 104, 111, 110, 32, 55357, 56333]`
* `[80, 121, 65, 84, 76, 32, 55356, 57169]`

### Tips:

* The core trick of this logic will be to write your loop so that if you find a surrogate (a number between 55,296 and 57,343), you jump to the next value and process the pair into a code before converting it to a character.
* You can assume that your input is correct, i.e. surrogates always come in valid pairs.
* All of those numbers look arbitrary but they make a lot more sense when written in [hexadecimal]. You can get the hexadecimal value of an integer using the `hex` function, and you can also write literal hexadecimal values in python using the `Ox` prefix. For example:

      hex(55296) == '0xd800'  # Strings
      0xd800 == 55296  # Integers

## Part 3: Combining pairs of bytes

In practice, data will be coming in as [bytes][byte], which are all numbers between 0 and 255 included. To build the codes that part 2 uses as input (all between 0 and 65,535 included), we need to put pairs of bytes together.

In this first implementation, _all_ our codes will be built by doing:

    code = first + second * 256

### Examples:

* the letter "X" (uppercase) has a code point of 88. It will come in as `[88, 0]`
* the sequence `[58, 38]` corresponds to the code point 38 × 256 + 58 = 9786, which is the smiling face emoji (&#9786;).

A few longer examples with strings:
* `"Hello!"` will come in as `[72, 0, 101, 0, 108, 0, 108, 0, 111, 0, 33, 0]`
* `"Mail ✉"` will come in as `[77, 0, 97, 0, 105, 0, 108, 0, 32, 0, 9, 39]` (the last character is the "envelope" symbol at U+2709 or code point 9993).

This is a step that happens _before_ what we did in part 2. For example, `[60, 216, 85, 223]` becomes `[55356, 57173]` which becomes `[127829]` (the pizza emoji again).

### Tests:

What are the strings behind:
* `[80, 0, 121, 0, 116, 0, 104, 0, 111, 0, 110, 0]`
* `[175, 0, 92, 0, 95, 0, 40, 0, 196, 48, 41, 0, 95, 0, 47, 0, 175, 0]`
* `[92, 38, 94, 38, 93, 38, 91, 38, 90, 38, 93, 38, 94, 38, 92, 38, 10, 0, 95, 38, 95, 38, 95, 38, 95, 38, 95, 38, 95, 38, 95, 38, 95, 38]`

### Tips:

You will need to figure out a way to process the input data by pairs. There are several (all valid) ways to do this!

1. Use an index (say `i`) that increments by 2, and access `data[i]` and `data[i+1]` at each step. `range(0, len(data), 2)` might be useful here.
2. Use `zip()` to combine the data with itself shifted by one step, like this:
    ```
    for first, second in zip(data[::2], data[1::2]):
        ...
    ```
3. Use variables to store the temporary values and keep track of whether you're looking at the first or second byte of a pair.

It might also be a good idea to check if you data has a even number of bytes, and throw an error if it does not.

## Part 4: Dealing with actual binary data

Binary data in Python is rarely manipulated using lists of numbers; instead Python uses [byte-strings](#strings-vs-bytes) (the `bytes` type). Can you modify your code so that it accepts byte-strings?

### Example:

The byte-string:

    b'P\x00i\x00z\x00z\x00a\x00 \x00<\xd8U\xdf \x00L\x00a\x00n\x00d\x00'

decodes into "Pizza &#127829; Land".

### Tests:

What are the strings behind:

* `b'P\x00y\x00A\x00T\x00L\x00 \x00J\x00a\x00m\x00'`
* `b'A\x00T\x00L\x00 \x00e& \x00P\x00y\x00t\x00h\x00o\x00n\x00!\x00 \x00=\xd8\r\xdc'`
* `b'(\x00o%\xb0\x00\xa1%\xb0\x00)\x00o%5\xfe \x00;%\x01%;%'`
* `b'\\&^&]&[&Z&]&^&\\&\n\x00_&_&_&_&_&_&_&_&'`
* `b'P\x00y\x00t\x00h\x00o\x00n\x00 \x00=\xd8\r\xdc'`
* `b'P\x00y\x00A\x00T\x00L\x00 \x00<\xd8Q\xdf'`

You can test your code against any string now! The `UTF-16LE` encoding should be compatible with it. Any string encoded that way (with `my_string.encode("UTF-16LE")`) should work. Most emoji use the higher code points, so you can have fun with that.

### Tips:

* `bytes` and list of numbers are more or less the same thing! Depending on how you implemented part 2, you might have nothing to change to make this work. If you want to convert `bytes` into a list, you can do so with `list()`.
* To write bytes in Python, it's the same as strings but with `b` in front of the string, as so: `b'Hello'`. Unlike normal string though, only ASCII characters are allowed, and everything else needs to use the `\xNN` hexadecimal escape sequence.
* Having trouble with the input? Make sure that you copy the strings correctly, the backslashes (`\`) are important and should all be included. Don't forget the `b` prefix either, otherwise you will be manipulating a string instead of bytes.

## Part 5: Dealing with byte order

Up until now we've assumed that our data was always little-endian, but UTF-16 allows it to be big-endian. In that case, any pair of bytes is read so that the first one is the high value, and the second is the lower. For example, the letter "X" is coded `b'\x88\x00'` in little-endian mode, and `b'\x00\x88'` in big-endian mode. Surrogate order is not affected.

The order is generally specified using a "Byte-Order Mark" (BOM) at the start of the data. The logic is:
1. if the data starts with `0xFFFE`, the order is little-endian (and those two first bytes are ignored);
2. if the data starts with `0xFEFF`, the order if big-endian (and the mark is also ignored);
3. otherwise, assume the order to be little-endian (and _do not_ ignore the first two bytes!).

Can you modify your code to automatically detect the byte-order?

### Example:

The byte-string:

    b'\xfe\xff\x00P\x00i\x00z\x00z\x00a\x00 \xd8<\xdfU\x00 \x00L\x00a\x00n\x00d'
 
decodes into "Pizza &#127829; Land" again.
 
## Extras

Congratulations, you now have a functional (but incomplete) [UTF-16] decoder! Here are some extra challenges if you found that fun:

* Write a UTF-16 encoder
* Allow the byte-order to be specified as an argument to the decoder
* Implement more complete error handling, failing to decode if anything looks wrong (invalid code point, incorrect use of surrogates, surrogates in wrong order, etc.).

Even more difficult challenges:

* Make your code raise correct `UnicodeDecodeError` exceptions. Those require the code to specify _where_ the failure happened, which might break a lot of your design assumptions.
* Allow error handling to be customized, the same way the built-in codecs work (e.g. replace invalid data with placeholder `U+FFFD` characters, and many more).
* Integrate your code and register your custom codec, [as documented in the `codecs`][python-codecs] standard library module.
* Do the same with [UTF-8]. It's a lot more complicated.

## Explanations

### What is Unicode?

[Unicode] is an universal encoding standard. In other words, it's **a database of all characters and symbols** from all writing systems (or at least the vast majority of the known ones).

In unicode, each character is assigned a unique **code point** (number). Code points can be any number up to 1,114,111 (21 bits), minus some reserved ranges. Those numbers are generally represented in [Hexadecimal] notation for convenience. For example, the code point 8364 is written U+20AC.

Wikipedia has a summarized list of the characters, and it can be found on a number of other websites:  
https://en.wikipedia.org/wiki/List_of_Unicode_characters

### What is an encoding?

Unicode code points are just numbers; they cannot be directly written in text files or to the network without some kind of data structure. It requires an intermediate step, called **coding**, to convert the Unicode code points into binary data (bytes).

The most popular way to code Unicode (by far) is [UTF-8]. It transforms each code point into a sequence of between one and four bytes, depending on how large the code point is. Its main advantage is to be compatible with the old [US-ASCII] standard. This means a file encoded with UTF-8 will have all ASCII characters (basic letters, digits and symbols) un-modified in it. The terms "UTF-8" and "Unicode" are sometimes erroneously mixed up because of how popular UTF-8 is.

The other well-known codec is [UTF-16], the one studied in this problem. Its approach is to encode every character over two bytes (four for code points over 16 bits, see [part 2](#part-2-dealing-with-large-code-points) for details). Consequently, unlike UTF-8 is is not compatible with ASCII. It's used by default in Java and the Windows operating system. In general, use of UTF-16 in file and over the internet is quite small.

The act of converting code points into bytes is called _encoding_, and the reverse operation is called _decoding_. Encoding to the Unicode codecs is generally straightforward, while decoding can easily fail if the binary data is corrupted (and you should assume that it will be).

### Working with Unicode in Python

#### Basics: Strings

In Python 3, [strings are immutable sequences of Unicode code points][python-str]. This the string:

    "Épices :\t2,85€"

is stored under the hood as an array with the code points:

    [201, 112, 105, 99, 101, 115, 32, 58, 9, 50, 44, 56, 53, 8364]

The string class thankfully provides a powerful abstraction layer so that we rarely have to be aware of that.

Python source files are expected to be UTF-8 encoded. This allows any valid Unicode character to be directly written inside the literal strings of your code! The interpreter knows how to handle Unicode natively.

Alternatively, you can write characters with their hexadecimal code point using escape sequences:

* `\xNN`: For code points up to 255. For example, `"\xc9"` is the same as `"É"`.
* `\uNNNN`: For code points up to 65,535. For example, `"\u20ac"` is the same as `"€"`.
* `\UNNNNNNNN`: For larger code points. For example, `"\U0001f44d"` is the "thumbs up" emoji.

**Note:** Python 2 is quite different in that regard. If you are a beginner, you should not be using Python 2 and you can safely ignore that complication.

#### Manipulating code points

Python has two built-in functions to query the code point of a character, and conversely transform a code point into a character object. Those are `ord()` and `chr()` respectively:

    >>> ord("a")
    97
    >>> ord("É")
    201
    >>> ord("€")
    8364
    >>> chr(97)
    'a'
    >>> chr(201)
    'É'
    >>> chr(8364)
    '€'
    >>> ord("\U0001f44d") == 0x1f44d
    True

Note that Python does not have a "character" type like most other languages; a string that is one character long is considered to be a character.

#### Strings vs. Bytes

One way to look at strings in Python is that they are "abstract" text. The way Python manipulates strings internally is an implementation detail that should be of no concern to Python programmers in general. 

However, as stated earlier Unicode itself cannot be stored or sent outside of your software's memory as-is. This is why Python includes a [separate data structure called `bytes`][python-bytes] to represent that binary data. These objects are represented as such:

    b'Hello world!'
    
But wait that's a string, right? Well, yes and no. No because `bytes` objects are sequences of numbers, fundamentally speaking. If you try to access an element of this object or iterate over it, you will get integers back:

    >>> b'Hello'[0]
    72
    >>> list(b'World')                                                          
    [87, 111, 114, 108, 100]

The reason it looks like a string is because any element in a `bytes` object that corresponds to the code point of a printable ASCII character is represented as such. So if your data is only made of ASCII text, its binary representation will look exactly the same.

This can be confusing. Keep in mind that those are very different data types. As a summary:

* `'Hello'` = The sequence of characters made of the letters H, e, l, l, and o. It is represented as numbers under the hood but we don't need to care how.
* `b'Hello'` = The sequence of numbers 72, 101, 108, 108, and 111. Which happen to be the ASCII codes for H, e, l, l, and o respectively.

In Python, having to manipulate bytes directly is generally uncommon. That is because most tools (e.g. opening text files, sending out HTTP requests) already deal with it! They either have some form of automatic encoding detection, or default to UTF-8. If you ever see an argument named `encoding` on a tool, it's to allow you to control that behavior when needed.

**Note:** Do not mix up binary strings (with the `b` prefix) with _"raw" strings_ (`r` prefix)! Raw strings are strings, only using a notation that tells the interpreter to not process escaping sequences:

* `'H\x65l\x6co'` is the same as `'Hello'` since U+65 and U+6C are the code points for 'e' and 'l';
* `r'H\x65l\x6co'` is the same as `'H\\x65l\\x6co'`, where using two backslashes in a row represents a literal backslash.

#### Encoding strings into bytes

The Python string class (`str`) provides the handy `.encode()` method. By default, it will encode strings using UTF-8. For example:

* `'Python'.encode()` returns `b'Python'`. They look identical because all characters are ASCII (code point ≤ 127), but that is generally not true. Case in point…
* Our first example `'Épices :\t2,85€'.encode()` returns `b'\xc3\x89pices :\t2,85\xe2\x82\xac'`. Here, the non-ASCII characters have been converted into sequences of non-printable bytes.

The `encode()` method accepts several arguments. The first allows other encodings to be used:

* `'Python'.encode('UTF-16LE')` returns `b'P\x00y\x00t\x00h\x00o\x00n\x00'`, a good illustration of UTF-16's incompatibility with ASCII.
* `'Épices :\t2,85€'.encode('iso-8859-15')` returns `b'\xc9pices :\t2,85\xa4'`. This may look similar to UTF-8, but it is not! Our non-ASCII characters are encoded as only one byte, as defined in that specific encoding.

We've seen several representations of the "É" character, here's a summary in case you're confused:
* `'\xc9'` is the _string_ `'É'`, where C9 is the _Unicode code point_ of that character (in hexadecimal),
* `b'\xc9'` is the _byte code_ for "É" in ISO-8859-1 (and ISO-8859-15). This is because all Unicode code points in the 0 to 255 range are based on ISO-8859-1, but that is a merely a coincidence.
* `b'\xc3\x89'` is the binary coding for "É" in UTF-8.

Encoding strings using non-Unicode encodings must be done carefully, because there is no guarantee that any Unicode character can be represented. For example, encoding the example above with "Latin-1" (a.k.a. [ISO-8859-1]) would have failed because it cannot process the "€" symbol.

Handling those errors is the purpose of the second argument in `.encode()`. It tells the codec what to do when something unexpected happens. By default a `UnicodeEncodeError` exception is raised ("strict") but you can also ignore invalid characters (to be used carefully) or replace them with a placeholder. [See the documentation][python-codecs-errors] for more details.

#### Decoding bytes into strings

Conversely, the `bytes` objects have a `.decode()` method to convert bytes into strings. By default, it behaves like the exact reverse of `str.encode()` and will try to decode the bytes using UTF-8, raising an exception if that fails:

* `b'Python'.decode()` returns `'Python'`.
* `b'\xc3\x89pices :\t2,85\xe2\x82\xac'.decode()` returns `'Épices :\t2,85€'`.
* `b'\xc9pices :\t2,85\xa4'.decode()` fails because it is not valid UTF-8.

However, decoding can fail in many more creative ways than encoding. In particular, UTF-8 is quite strict and random binary data (that was not encoded with UTF-8) has a very high chance to fail when decoded. Like `str.encode()`, various error handling modes are available. If you are decoding UTF-8 or UTF-16 data that's even remotely un-trusted, proper error handling is _essential_.

Older codecs have the reverse problem; practically any byte correctly matches a character. Decoding with the wrong codec _will_ lead to incorrect data. In particular, decoding UTF-8 in that way results in interesting artifacts. For example, `'Épices :\t2,85€'.encode("utf-8").decode("cp1252")` returns `'Ã‰pices :\t2,85â‚¬'`.

In short, be careful when you decode text data.

[Hexadecimal]: https://simple.wikipedia.org/wiki/Hexadecimal
[Unicode]: https://home.unicode.org/
[Byte]: https://en.wikipedia.org/wiki/Byte
[UTF-8]: https://en.wikipedia.org/wiki/UTF-8
[UTF-16]: https://en.wikipedia.org/wiki/UTF-16
[US-ASCII]: https://en.wikipedia.org/wiki/ASCII
[ISO-8859-1]: https://en.wikipedia.org/wiki/ISO/IEC_8859-1
[python-str]: https://docs.python.org/3.8/library/stdtypes.html#textseq
[python-bytes]: https://docs.python.org/3/library/stdtypes.html#bytes-objects
[python-codecs]: https://docs.python.org/3.8/library/codecs.html
[python-codecs-errors]: https://docs.python.org/3.8/library/codecs.html#error-handlers