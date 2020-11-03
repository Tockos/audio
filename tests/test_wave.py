
import sys
sys.path.append("../")

import unittest
from itertools import zip_longest
from numpy.testing import *
from audio.wave import Wave


BIG = list(range(2**15))
TEST_ARRAYS = (
    ([], []),
    ([], [1]),
    ([], [1, 2]),
    ([], BIG),

    ([0], []),
    ([0], [1]),
    ([0], [1, 2]),
    ([0], BIG),

    ([0, 1], []),
    ([0, 1], [2]),
    ([0, 1], [2, 3]),
    ([0, 1], BIG),

    (BIG, []),
    (BIG, [2]),
    (BIG, [2, 3]),
    (BIG, BIG),
)


class TestWave(unittest.TestCase):

    # -------------------------------------------------------------------------
    # Extend:
    # -------------------------------------------------------------------------
    def test_extend_right(self):
        for base, extra in TEST_ARRAYS:
            try:
                a = Wave(base)
                a.extend(extra)
                b = Wave(base + extra)
                self.assertEqual(a, b)
            except AssertionError:
                print("base: %s, extra: %s, result: %s" % (base, extra, base+extra))
                raise

    def test_extend_left(self):
        for base, extra in TEST_ARRAYS:
            try:
                a = Wave(base)
                a.extend(extra, left=True)
                b = Wave(base + extra)
                self.assertEqual(a, b)
            except AssertionError:
                print("base: %s, extra: %s, result: %s" % (base, extra, base+extra))
                raise

    # -------------------------------------------------------------------------
    # Shift:
    # -------------------------------------------------------------------------
    def test_shift_left(self):
        pass

    def test_shift_right(self):
        pass

    # -------------------------------------------------------------------------
    # Add:
    # -------------------------------------------------------------------------
    def test_add(self):
        for a1, a2 in TEST_ARRAYS:
            try:
                result = [x+y for x, y in zip_longest(a1, a2, fillvalue=0)]
                self.assertEqual(Wave(a1) + Wave(a2), Wave(result))
            except:
                print("a: %s, b: %s, result: %s" % (a1, a2, result))
                raise

    # -------------------------------------------------------------------------
    # Norm:
    # -------------------------------------------------------------------------
    def test_norm(self):
        pass


if __name__ == "__main__":
    unittest.main()

