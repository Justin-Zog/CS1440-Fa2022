from Fractal import Fractal


class Phoenix(Fractal):
    def __init__(self, max_iter, j_const, p_const):
        self.__max_iter = max_iter
        self.j_const = j_const
        self.p_const = p_const

    def count(self, complex_number):
        complex_number = complex(complex_number.imag, complex_number.real)
        prev_z = complex(0, 0)

        for i in range(self.__max_iter):
            z_save = complex_number
            complex_number = complex_number * complex_number + self.j_const + (self.p_const * prev_z)
            prev_z = z_save

            if abs(complex_number) > 2:
                return i

        # If 'z' never grew greater than 2, then the coordinate is bounded
        return self.__max_iter - 1
