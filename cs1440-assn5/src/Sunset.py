from colour import Color
from Palette import Palette

# Sunset Colors
SUNSET_YELLOW = Color('#eeaf61')
SUNSET_ORANGE = Color('#fb9062')
STRAWBERRY_LEMONADE = Color('#ee5d6c')
PINK = Color('#ce4993')
PURPLE = Color('#6a0d83')


class Sunset(Palette):
    def __init__(self, size):
        super().__init__(size)
        self.palette = [color.hex_l for color in SUNSET_YELLOW.range_to(PURPLE, int(size / 7))]
        self.palette += [color.hex_l for color in PURPLE.range_to(SUNSET_ORANGE, int(size / 7))][1:]
        self.palette += [color.hex_l for color in SUNSET_ORANGE.range_to(PURPLE, int(size / 7))][1:]
        self.palette += [color.hex_l for color in PURPLE.range_to(STRAWBERRY_LEMONADE, int(size / 7))][1:]
        self.palette += [color.hex_l for color in STRAWBERRY_LEMONADE.range_to(PURPLE, int(size / 7))][1:]
        self.palette += [color.hex_l for color in PURPLE.range_to(PINK, int(size / 7))][1:]
        self.palette += [color.hex_l for color in PINK.range_to(PURPLE, int(1 + self.size - len(self.palette)))][1:]

    def getColor(self, n) -> str:
        # n is an integer and this function should return a string
        return self.palette[n]
