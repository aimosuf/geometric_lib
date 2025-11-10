import unittest
import math
import circle   
import square  

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        res = circle.area(1)
        self.assertAlmostEqual(res, math.pi, places=7)

    def test_area_negative_current_behavior(self):
        res = circle.area(-3)
        self.assertAlmostEqual(res, 9 * math.pi, places=7)

    def test_perimeter_zero(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        res = circle.perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi, places=7)

    def test_perimeter_negative_current_behavior(self):
        res = circle.perimeter(-3)
        self.assertAlmostEqual(res, -6 * math.pi, places=7)


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    def test_area_negative_current_behavior(self):
        res = square.area(-3)
        self.assertEqual(res, 9)

    def test_perimeter_zero(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)

    def test_perimeter_negative_current_behavior(self):
        res = square.perimeter(-3)
        self.assertEqual(res, -12)