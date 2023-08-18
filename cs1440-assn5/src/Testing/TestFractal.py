#!/usr/bin/env python3

import unittest
from Fractal import Fractal


class TestFractal(unittest.TestCase):

    def test_abstract(self):
        with self.assertRaises(NotImplementedError):
            Fractal()
        with self.assertRaises(NotImplementedError):
            Fractal().count()


if __name__ == '__main__':
    unittest.main()
