from unittest import TestCase
from triangle import Triangle

class TestTriangle(TestCase):
    def test_Triangle(self):
        self.assertEqual(Triangle(4, 8), 16)
        self.assertEqual(Triangle(6, 2), 6)
        self.assertEqual(Triangle(2, 4), 4)
        self.fail()
