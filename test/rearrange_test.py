#!/usr/bin/env python3

from cgi import test
from cmath import exp
from rearrange import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):

    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty_string(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Johnson, Mike R."
        expected = "Mike R. Johnson"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()
