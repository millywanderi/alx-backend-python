#!/usr/bin/env python3
"""
A module that parameterize a unit test
"""
import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch
from typing import Dict, Tuple, Union
from utils import access_nested_map, get_jason, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests `access_nested_map` function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected_result: Union[Dict, int],
            ) -> None:
        """A method that parameterize a unit test"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), keyError),
        ({"a": 1}, ("a", "b"), keyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
    """Tests `test_access_nested_map` exception raising"""
    with self.assertRaises(exception):
        access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """class that test that utils.get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", test_payload={"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """Tests `get_json` function"""
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)
