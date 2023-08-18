#!/usr/bin/env python3

import unittest
from Palette import Palette
from Ocean import Ocean
from Sunset import Sunset
from Forest import Forest


class TestPalette(unittest.TestCase):

    def test_abstract(self):
        with self.assertRaises(NotImplementedError):
            Palette(size=110).getColor(5)

    def test_color(self):
        self.assertEqual(Ocean.getColor(Ocean(10), 0), '#cff5e7')
        self.assertEqual(Forest.getColor(Forest(10), 0), '#557153')
        self.assertEqual(Sunset.getColor(Sunset(10), 0), '#eeaf61')


if __name__ == '__main__':
    unittest.main()
