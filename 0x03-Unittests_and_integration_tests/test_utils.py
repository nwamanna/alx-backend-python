#!/usr/bin/env python3
""" a TestAccessNestedMap class that inherits from
    unittest.TestCase.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """ Implement the TestAccessNestedMap.test_access_nested_map
        method to test that the method returns what it is
    """
    @parameterized.expand([
                            ({"a": 1}, ("a",), 1),
                            ({"a": {"b": 2}}, ("a",), {"b": 2}),
                            ({"a": {"b": 2}}, ("a", "b"),  2)
    ])
    def test_access_nested_map(self, a: Mapping, b: Sequence, expected: int):
        result = access_nested_map(a, b)
        self.assertEqual(result, expected)
