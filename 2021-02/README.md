# Chess Notation Decoder

PyATL Jam Session - February 4th, 2021

## 1. Coordinates Notation

### 1.1. Introduction

Let's start with a simple approach: we will be representing each move by its
full start and destination coordinates.  This notation should be unambiguous and
(mostly) require little  knowledge of the rules of chess to interpret: take the
piece on the start square to the destination square, and capture the piece there
if it is occupied.  Repeat.  You can assume that the given instructions are
correct and always represent a legal move.

Each square on the board is identified by a letter and a digit.  With the black
pieces placed at the top of the board and the white pieces at the bottom, the
letter is the column (or "file") of that square, and the digit is its row
(or "rank").  Squares are numbered left to right and bottom to top, such that:

* `a1` is the bottom-left square
* `h1` is the top-left square
* `a8` is the bottom-right square
* `h8` is the top-right square

```
   a b c d e f g h
8  ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜  8  Black
7  ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎  7
6                   6
5                   5  
4                   4
3                   3
2  ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙  2
1  ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖  1  White
   a b c d e f g h
````

We will represent a move as 4 characters, where the two pairs of characters are
the start and destination coordinates respectively.  For example, `e2e4` means
"the piece on square `e2` moves to square `e4`".  At the start of the game, that
move would be to advance the white pawn ♙ in file `e` by two squares.

### 1.2. Example

Here is a short example below.  What does the board look like at the end?

    e2e4 e7e5
    g1f3 b8c6
    d2d4 e5d4
    f3d4 f8c5
    c2c3 d8f6
    d4c6 f6f2

Game: [xQc vs. MoistCr1tikal, 2020-06-09](
    https://www.chess.com/news/view/chesscom-pogchamps-xqc-moistcr1tikal
)

### 1.3. Tips

For this first example, you do not need to understand or model any of the rules
of chess.  You will need:

1. a model for the 8x8 board, for example a 2D array
2. a model for the pieces, for example a string
3. code that can read the move instructions, and execute them.

### 1.4. More rules

There are a couple of notable edge cases:

* when a pawn ♟ is [promoted] (reaches the other side of the board), the piece
  it was replaced with is specified by adding a character:  Q for queen ♛, R for
  rook ♜, B for bishop ♝, and N for knight ♞;
  
* when [castling], the start and end positions of the king ♚ are recorded, and
  the rook ♜ move is implied:
  * `e1c1`:  queenside white castling (rook moved from `a1` to `d1`)
  * `e1g1`:  kingside white castling (rook moved from `h1` to `f1`)
  * `e8c8`:  queenside black castling (rook moved from `a8` to `d8`)
  * `e8g8`:  kingside black castling (rook moved from `h8` to `f8`)

There are some other cases that exist, but we will ignore those.

### 1.5. Longer example

With this knowledge in mind, reconstitute the game in `game_coordinates.txt`.

* What does the board look like right before Black's 30th move?
* And what does it look like at the end of the game? 
  
Note that it includes examples of both castling and pawn promotion.

Game: [Alphamaxnova1 vs. anonymous, 2020-06-17](https://lichess.org/a6wPfCpl)

## 2. Algebraic Notation

**Note: This is a much more challenging puzzle, for the curious folks who want
to play more with chess programming stuff.**

While coordinates notation is easy to work with, it is difficult for humans to
understand.  To know which piece has been moved and what that move did, one must
keep a full picture of the board at all times.

In practice, the [algebraic notation] is the most widely used.  It is designed
to be concise and precise but still fairly readable:

* the piece being moved is indicated by a letter,
* only the destination square is specified in most cases,
* captures, checks and checkmate are indicated with additional symbols,
* moves are numbered for easier look-ups.

The full specification if fairly complex and can be found online;  you will be
expected to do some research.

For example, the short game from earlier is written as:

    1. e4 e5  
    2. Nf3 Nc6  
    3. d4 exd4  
    4. Nxd4 Bc5  
    5. c3 Qf6  
    6. Nxc6 Qxf2#

This can be read as:

1. White pawn (in e2) moves to e4, black pawn (in e7) moves to e5
2. White knight (in g1) moves to f3, black knight (in b8) moves to c6
3. White pawn (in d2) moves to d4, black pawn (in e5) captures it right after
4. White knight (previously moved to f3) captures the black pawn in d4, then
   black bishop (in f8) moves to c5
5. White pawn (in c2) moves to c3, black queen (in d8) moves to f6
6. White knight (in d4) captures black knight in c6, finally black queen (in f6)
   captures white pawn in f2 and puts the white king in checkmate doing so.

The difficulty here is that the starting piece and position have to be inferred
from which pieces _can_ move to the destination square.  While this if fairly
easy for a human looking at the board (and who knows the rules), it requires a
lot more work for a computer to figure out.

Challenge:  Write code that can understand algebraic notation!  A version of the
longer game from earlier can be found in `game_algebraic.pgn`

[algebraic notation]: https://en.wikipedia.org/wiki/Algebraic_notation_(chess)
[castling]: https://en.wikipedia.org/wiki/Castling
[checkmate]: https://en.wikipedia.org/wiki/Checkmate
[promoted]: https://en.wikipedia.org/wiki/Promotion_(chess)