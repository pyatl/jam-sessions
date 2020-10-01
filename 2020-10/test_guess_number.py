import runpy
from unittest import TestCase, mock

from mystery_number import NumberGuessGame


class TestGuessnumber(TestCase):
    def test_any_number(self):
        """Test that it works in general"""
        number = NumberGuessGame()
        with mock.patch("mystery_number.guess_number", side_effect=number):
            runpy.run_module("guess_number")
        self.assertTrue(number.success, msg="You failed to guess the number")

    def test_number_zero(self):
        """Test that an number of one is supported"""
        number = NumberGuessGame(1)
        with mock.patch("mystery_number.guess_number", side_effect=number):
            runpy.run_module("guess_number")
        self.assertTrue(number.success, msg="An number of 1 must work")

    def test_number_hundred(self):
        """Test that an number of 100 is supported"""
        number = NumberGuessGame(100)
        with mock.patch("mystery_number.guess_number", side_effect=number):
            runpy.run_module("guess_number")
        self.assertTrue(number.success, msg="An number of 100 must work")

    def test_fast_runtime(self):
        """Test that the code is fast!"""
        for _ in range(10):
            number = NumberGuessGame(quiet=True)
            with mock.patch("mystery_number.guess_number", side_effect=number):
                runpy.run_module("guess_number")
            # In theory only 7 guesses are ever needed, we'll allow a
            # few more to account for implementation edge cases.
            self.assertLessEqual(number.attempts, 10, msg="You can do it faster!")
