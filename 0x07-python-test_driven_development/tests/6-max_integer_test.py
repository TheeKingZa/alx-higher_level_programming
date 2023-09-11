import unittest
from my_module import max_integer  # Import the function to be tested

class TestMaxInteger(unittest.TestCase):
    def test_max_integer_positive(self):
        # Test with a list of positive integers
        result = max_integer([1, 3, 5, 2, 4])
        self.assertEqual(result, 5)

    def test_max_integer_negative(self):
        # Test with a list of negative integers
        result = max_integer([-10, -5, -8, -2])
        self.assertEqual(result, -2)

    def test_max_integer_mixed(self):
        # Test with a list of mixed positive and negative integers
        result = max_integer([-5, 3, -8, 10, 2])
        self.assertEqual(result, 10)

    def test_max_integer_single_element(self):
        # Test with a list containing a single element
        result = max_integer([42])
        self.assertEqual(result, 42)

    def test_max_integer_empty_list(self):
        # Test with an empty list (should return None)
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_integer_floats(self):
        # Test with a list of floats (should raise a TypeError)
        with self.assertRaises(TypeError):
            max_integer([1.5, 2.7, 3.3])

    def test_max_integer_strings(self):
        # Test with a list of strings (should raise a TypeError)
        with self.assertRaises(TypeError):
            max_integer(["apple", "banana", "cherry"])

if __name__ == '__main__':
    unittest.main()

