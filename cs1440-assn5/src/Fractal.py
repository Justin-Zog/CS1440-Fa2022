class Fractal:
    # Abstract constructor to prevent a Fractal object from ever being created.
    def __init__(self):
        raise NotImplementedError("Fractal is not concrete and can not have a 'max_iter'.")

    def count(self, complex_number):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")
