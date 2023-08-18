from Mandelbrot import Mandelbrot
from Phoenix import Phoenix
from Julia import Julia
from Spider import Spider


def makeFractal(fractal_info):
    if fractal_info['type'] == 'mandelbrot':
        return Mandelbrot(fractal_info['iterations'])
    elif fractal_info['type'] == 'phoenix':
        return Phoenix(fractal_info['iterations'], complex(fractal_info['creal'], fractal_info['cimag']), complex(fractal_info['preal'], fractal_info['pimag']))
    elif fractal_info['type'] == 'julia':
        return Julia(fractal_info['iterations'], complex(fractal_info['creal'], fractal_info['cimag']))
    elif fractal_info['type'] == 'spider':
        return Spider(fractal_info['iterations'])
    else:
        raise NotImplementedError(f"This program cannot create a fractal of type '{fractal_info['type']}'")
