import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_instance_creation(self):
        r1 = Rectangle(4, 6)
        r2 = Rectangle(2, 3, 1, 1, 10)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 1)
        self.assertEqual(r2.id, 10)

    def test_width_setter(self):
        r = Rectangle(4, 6)
        r.width = 10
        self.assertEqual(r.width, 10)

    def test_area(self):
        r = Rectangle(4, 6)
        self.assertEqual(r.area(), 24)

    def test_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        self.assertEqual(r.display(), expected_output)

    def test_update(self):
        r = Rectangle(4, 6)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

if __name__ == '__main__':
    unittest.main()
