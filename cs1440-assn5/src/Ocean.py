from colour import Color
from Palette import Palette

NAVY = Color('#021d47')
# Ocean Colors
SEAFOAM_GREEN = Color('#cff5e7')
DARK_SEAFOAM = Color('#a0e4cb')
TEAL = Color('#59c1bd')
CERULEAN = Color('#02a4d3')


class Ocean(Palette):
    def __init__(self, size):
        super().__init__(size)
        self.palette = [color.hex_l for color in SEAFOAM_GREEN.range_to(NAVY, int(size / 7))]
        self.palette += [color.hex_l for color in NAVY.range_to(DARK_SEAFOAM, int(size / 7))][1:]
        self.palette += [color.hex_l for color in DARK_SEAFOAM.range_to(NAVY, int(size / 7))][1:]
        self.palette += [color.hex_l for color in NAVY.range_to(TEAL, int(size / 7))][1:]
        self.palette += [color.hex_l for color in TEAL.range_to(NAVY, int(size / 7))][1:]
        self.palette += [color.hex_l for color in NAVY.range_to(CERULEAN, int(size / 7))][1:]
        self.palette += [color.hex_l for color in CERULEAN.range_to(NAVY, int(1 + self.size - len(self.palette)))][1:]

    def getColor(self, n) -> str:
        # n is an integer and this function should return a string
        return self.palette[n]
