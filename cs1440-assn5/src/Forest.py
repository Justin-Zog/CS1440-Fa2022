from colour import Color
from Palette import Palette

DARK_OAK = Color('#362419')
# Forest Colors
DEEP_FOREST_GREEN = Color('#557153')
NATURE_GREEN = Color('#7d8f69')
BROWN_GREEN = Color('#a9af7e')
YELLOW_GREEN = Color('#e6e5a3')


class Forest(Palette):
    def __init__(self, size):
        super().__init__(size)
        self.palette = [color.hex_l for color in DEEP_FOREST_GREEN.range_to(DARK_OAK, int(size / 7))]
        self.palette += [color.hex_l for color in DARK_OAK.range_to(NATURE_GREEN, int(size / 7))][1:]
        self.palette += [color.hex_l for color in NATURE_GREEN.range_to(DARK_OAK, int(size / 7))][1:]
        self.palette += [color.hex_l for color in DARK_OAK.range_to(BROWN_GREEN, int(size / 7))][1:]
        self.palette += [color.hex_l for color in BROWN_GREEN.range_to(DARK_OAK, int(size / 7))][1:]
        self.palette += [color.hex_l for color in DARK_OAK.range_to(YELLOW_GREEN, int(size / 7))][1:]
        self.palette += [color.hex_l for color in YELLOW_GREEN.range_to(DARK_OAK, int(1 + self.size - len(self.palette)))][1:]

    def getColor(self, n) -> str:
        # n is an integer and this function should return a string
        return self.palette[n]
