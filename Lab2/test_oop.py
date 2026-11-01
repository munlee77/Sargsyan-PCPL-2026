import unittest
import math
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

class TestGeometricFigures(unittest.TestCase):

    def test_rectangle_square(self):
        r = Rectangle(4, 5, "синий")
        self.assertEqual(r.square(), 20)

    def test_circle_square(self):
        c = Circle(3, "зеленый")
        self.assertAlmostEqual(c.square(), math.pi * 9)

    def test_square_square(self):
        s = Square(4, "красный")
        self.assertEqual(s.square(), 16)

if __name__ == '__main__':
    unittest.main()
