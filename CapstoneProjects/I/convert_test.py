#!/usr/bin/env python3

from convert import get_images_as_list
from convert import rotate_scale as rotate
import unittest



class TestRearrange(unittest.TestCase):

    def test_is_list(self):
        image_list = get_images_as_list()
        self.assertIsInstance(image_list, list)

unittest.main()