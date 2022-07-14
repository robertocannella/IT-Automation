#!/usr/bin/env python3

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
    
    def test_one_name(self):
        testcase = "Roberto"
        expected = "Roberto"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_invalid_input(self):
        self.assertRaises(ValueError, rearrange_name, 1234)
unittest.main()
