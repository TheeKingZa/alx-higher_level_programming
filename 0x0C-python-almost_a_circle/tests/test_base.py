import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestBase(unittest.TestCase):

    def test_instance_creation(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_instance_with_custom_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_to_json_string(self):
        r1 = Rectangle(1, 2)
        json_string = Base.to_json_string([r1.to_dictionary()])
        self.assertEqual(json_string, '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]')

    def test_from_json_string(self):
        """Test from_json_string method."""
        json_string = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]'
        list_dicts = Base.from_json_string(json_string)
        instances = [Rectangle.create(**d) for d in list_dicts]
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[0].width, 2)
        self.assertEqual(instances[0].height, 3)
        self.assertEqual(instances[0].x, 4)
        self.assertEqual(instances[0].y, 5)

if __name__ == '__main__':
    unittest.main()
