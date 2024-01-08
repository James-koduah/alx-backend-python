#!/usr/bin/env python3
"""bla blah blah blah blah"""

import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """unit tests for nested map method"""

    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nestedMap, path, result):
        """testing the access_nested_map function"""
        self.assertEqual(access_nested_map(nestedMap, path), result)
