from Fractal import Fractal


class Spider(Fractal):
    def __init__(self, max_iter):
        self.__max_iter = max_iter

    def count(self, complex_number):
        z = complex(0, 0)

        for i in range(self.__max_iter):
            z = z * z + complex_number
            complex_number = ((complex_number / 2) + z)

            if abs(z) > 2:
                return i

        # If 'z' never grew greater than 2, then the coordinate is bounded
        return self.__max_iter - 1
