class Palette:

    def __init__(self, size):
        self.size = size
        self.palette = None

    def getColor(self, n) -> str:
        raise NotImplementedError("Concrete subclass of Palette must implement getColor() method")
