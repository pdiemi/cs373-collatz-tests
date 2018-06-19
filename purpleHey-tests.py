
#!/usr/bin/env python3

# pylint: disable=invalid-name

# ----------------------
# collatz/TestCollatz.py
# Copyright (C) 2018
# Glenn P. Downing
# ----------------------

"""
Unit and Application test harnass
"""

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_build_cache

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    """
    REP unit test cases
    """
    # ----
    # read
    # ----

    def test_read(self):
        """
        Test reader: verify that the tuple returned matchs what in the range passed in
        """

        range_str = "1 10\n"
        i, j = collatz_read(range_str)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        Test a range - note that we need to call the build cache method here
        otherwise the cache is empty.  There may be better way?  It seems if 
        I call it once, its there for the other tests.  There may be a 
        better way to do that too.
        """

        collatz_build_cache(1)
        range_str = collatz_eval(1, 10)
        self.assertEqual(range_str, 20)

    def test_eval_2(self):
        """
        Test a range
        """

        range_str = collatz_eval(100, 200)
        self.assertEqual(range_str, 125)

    def test_eval_3(self):
        """
        Test a range
        """

        range_str = collatz_eval(201, 210)
        self.assertEqual(range_str, 89)

    def test_eval_4(self):
        """
        Test a range
        """

        range_str = collatz_eval(900, 1000)
        self.assertEqual(range_str, 174)

    def test_eval_5(self):
        """
        Test a range where both values are greater than my cache value
        """

        range_str = collatz_eval(156158, 200000)
        self.assertEqual(range_str, 383)  # CL for 156159

    def test_eval_51(self):
        """
        Test a range where the first value is exactly the value of my
        max cache value.
        """

        range_str = collatz_eval(100000, 100004)
        self.assertEqual(range_str, 129)  # CL for 100000

    def test_eval_6(self):
        """
        Test a range
        """

        range_str = collatz_eval(1, 100000)
        self.assertEqual(range_str, 351)  # CL for 77031

    def test_eval_7(self):
        """
        Test a range that only 1 long
        """

        range_str = collatz_eval(837799, 837799)
        self.assertEqual(range_str, 525)  # CL for 837799

    def test_eval_8(self):
        """
        Test a range where the max value is the first
        value in the range.
        """

        range_str = collatz_eval(9, 11)
        self.assertEqual(range_str, 20)  # CL for 9

    def test_eval_9(self):
        """
        Test a range where the max value is the last value
        in the range
        """

        range_str = collatz_eval(13, 14)
        self.assertEqual(range_str, 18)  # CL for 14

    # -----
    # print
    # -----

    def test_print(self):
        """
        Test collatz_print: create a stringIO object and check
        """

        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """
        Run collatz passing in an set of range problems, solving, then
        comparing the output to the known right answer.
        """
        read_string_io = StringIO(
            "1 200000\n1 10\n100 200\n201 210\n900 1000\n")
        write_string_io = StringIO()
        collatz_solve(read_string_io, write_string_io)
        self.assertEqual(write_string_io.getvalue(),
                         "1 200000 383\n1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----


if __name__ == "__main__":  # pragma: no cover
    main()
