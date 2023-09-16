#!/usr/bin/python3
"""
Unit tests for the Rectangle class.
"""
import sys
import os
import unittest
import io
from unittest.mock import patch
from models.rectangle import Rectangle

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
# Add Parent dir of project to sys.path
class TestRectangle(unittest.TestCase):
    def test_area(self):
        # Test the area calculation
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_display(self):
        # Test the display method
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        # Test the custom string representation
        r = Rectangle(4, 5, 1, 2, 42)
        expected_str = "[Rectangle] (42) 1/2 - 4/5"
        self.assertEqual(str(r), expected_str)

    def test_update_args(self):
        # Test updating attributes using args
        r = Rectangle(4, 5, 1, 2, 42)
        r.update(10, 6, 7)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 7)

    def test_update_kwargs(self):
        # Test updating attributes using kwargs
        r = Rectangle(4, 5, 1, 2, 42)
        r.update(width=8, height=9)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 9)

if __name__ == '__main__':
    unittest.main()
