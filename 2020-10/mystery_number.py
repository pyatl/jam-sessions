# This is the code behind the guessing game. You do not need to edit
# or worry about this, your code is expected to be in guess_number.py
import random

class NumberGuessGame:
    def __init__(self, value: int = None, quiet=False):
        self.number: int = random.randint(1, 100) if value is None else value
        self.attempts = 0
        self.quiet = quiet
        self.success = False

    def __call__(self, guess: int):
        if self.attempts > 100:
            print("You tried too many times! Your strategy is not working.")
            raise RuntimeError()

        self.attempts += 1
        if guess == self.number:
            if not self.quiet:
                print(f"My number was {self.number}, that's correct!")
                print(f"It took you {self.attempts} attempts to get it right")
            self.success = True
            return "correct"

        elif guess > self.number:
            if not self.quiet:
                print(f"Wrong! My number is less than {guess}")
            return "too large"

        else:  # guess < number
            if not self.quiet:
                print(f"Wrong! My number is more than {guess}")
            return "too small"

guess_number = NumberGuessGame()
