# Tests for the sorting challenge.

import random
import runpy
from unittest import TestCase, mock, skip


class TestSorting(TestCase):

    def assert_sorting_works(self, list_to_sort, msg="The list is not sorted"):
        expected_list = list(sorted(list_to_sort))

        def fail_sort(*_, **__):
            error = "No cheating allowed, implement sorting yourself!"
            raise RuntimeError(error)

        almost_list = type("list", (list,), {"sort": fail_sort})
        list_to_sort = almost_list(list_to_sort)
        init_globals = {"list": almost_list, "sorted": fail_sort}

        with mock.patch("mystery_list.list_to_sort", list_to_sort):
            globs = runpy.run_module("sorting", init_globals=init_globals)

        output_list = globs["list_to_sort"]
        self.assertEqual(expected_list, output_list, msg=msg)

    def assert_random_sort(self, n):
        test_list = [random.randint(-2 * n, 2 * n) for _ in range(n)]
        self.assert_sorting_works(test_list)

    def test_example(self):
        """Test the example list in mystery_list.py"""
        from mystery_list import list_to_sort

        self.assert_sorting_works(list_to_sort)

    def test_random_10(self):
        """Test a random list of 10 numbers"""
        self.assert_random_sort(10)

    def test_random_100(self):
        """Test a random list of 100 numbers"""
        self.assert_random_sort(100)

    def test_random_1000(self):
        """Test a random list of 1,000 numbers"""
        self.assert_random_sort(1000)

    def test_list_already_sorted(self):
        """Test trying to sort an already sorted list"""
        self.assert_sorting_works(
            list(range(100)), "Did not work on an already-sorted list"
        )

    def test_one_element(self):
        """Test sorting a list with only one item"""
        self.assert_sorting_works([71], "Did not work on a one-element list")

    def test_empty_list(self):
        """Test sorting the empty list"""
        self.assert_sorting_works([], "Did not work on the empty list")

    # Is your code really fast? Remove the line below to find out!
    @skip("Tests a much longer list, enable this to really push your code")
    def test_very_long_list(self):
        n = 100000  # Edit this to try different sizes
        list_to_sort = [random.randint(-2 * n, 2 * n) for _ in range(n)]
        runpy.run_module("sorting", init_globals={"list": list_to_sort})
