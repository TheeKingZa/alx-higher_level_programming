#!/usr/bin/python3
"""Unit tests for Base class."""
import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_instance_creation(self):
        """Test creating a Base instance with and without an ID."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(100)
        self.assertEqual(b3.id, 100)

    def test_to_json_string(self):
        """Test the to_json_string method of Base class."""
        b1 = Base(1)
        b2 = Base(2)
        b3 = Base(3)

        dict_list = [b1.to_dictionary(), b2.to_dictionary(), b3.to_dictionary()]
        json_string = Base.to_json_string(dict_list)

        expected_json_string = json.dumps([{
            "id": 1,
            "width": 1,
            "height": 1,
            "x": 0,
            "y": 0
        }, {
            "id": 2,
            "width": 1,
            "height": 1,
            "x": 0,
            "y": 0
        }, {
            "id": 3,
            "width": 1,
            "height": 1,
            "x": 0,
            "y": 0
        }])

        self.assertEqual(json_string, expected_json_string)

    def test_from_json_string(self):
        """Test the from_json_string method of Base class."""
        json_string = '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]'
        dict_list = Base.from_json_string(json_string)

        expected_dict_list = [{
            "id": 1,
            "width": 1,
            "height": 2,
            "x": 0,
            "y": 0
        }]

        self.assertEqual(dict_list, expected_dict_list)


if __name__ == '__main__':
    unittest.main()
