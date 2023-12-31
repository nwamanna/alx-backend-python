#!/usr/bin/env python3
""" a TestAccessNestedMap class that inherits from
    unittest.TestCase.
"""
import requests
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
import utils
from utils import memoize
from typing import Mapping, Sequence, Callable, Dict


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
        result = utils.access_nested_map(a, b)
        self.assertEqual(result, expected)

    @parameterized.expand([
                            ({}, ("a",), KeyError),
                            ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, a: Mapping, b: Sequence,
                                         expected: type = KeyError):
        """ to test that a KeyError is raised for the following inputs """
        with self.assertRaises(expected):
            utils.access_nested_map(a, b)


class TestGetJson(unittest.TestCase):
    """ class to test get_json """
    @parameterized.expand([
                           ("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, url: str, expected: Dict, mock_request: Callable):
        # create a mock response
        mock_response = Mock()
        mock_response.json.return_value = expected

        # configure the patched requests to return the Mock value
        mock_request.return_value = mock_response

        response = utils.get_json(url)

        # test
        requests.get.assert_called_once_with(url)
        self.assertEqual(response, expected)


class TestMemoize(unittest.TestCase):
    """ class with a test_memoize method """
    def test_memoize(self):
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test = TestClass()
        with patch.object(test, 'a_method',
                          return_value=54) as mock_method:
            # call method
            val_1 = test.a_property
            val_2 = test.a_property

            # verify that the method was called only once
            mock_method.assert_called_once()

            # verify results are the same
            self.assertEqual(val_1, 54)
            self.assertEqual(val_2, 54)
