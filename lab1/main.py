import math
from unittest import TestCase


def circle_len(r):
    if r > 0:
        return 2 * math.pi * r
    else:
        return 0


class Test(TestCase):
    def test_positive_r(self):
        self.assertEqual(circle_len(2), 2*2*math.pi)
        self.assertTrue(circle_len(4) > 0)

    def test_negative_r(self):
        self.assertTrue(circle_len(-4) == 0)

    def test_zero_r(self):
        self.assertTrue(circle_len(0) == 0)
