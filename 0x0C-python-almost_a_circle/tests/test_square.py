import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_instance_creation(self):
        s1 = Square(5)
        s2 = Square(7, 2, 3, 10)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s2.size, 7)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 10)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        s = Square(3)
        expected_output = "###\n###\n###\n"
        self.assertEqual(s.display(), expected_output)

    def test_update(self):
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

if __name__ == '__main__':
    unittest.main()
