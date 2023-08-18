from Fractal import Fractal


class Julia(Fractal):
    def __init__(self, max_iter, j_const):
        self.__max_iter = max_iter
        self.j_const = j_const

    def count(self, complex_number):

        for i in range(self.__max_iter):
            complex_number = complex_number * complex_number + self.j_const

            if abs(complex_number) > 2:
                return i

        # If 'z' never grew greater than 2, then the coordinate is bounded
        return self.__max_iter - 1
