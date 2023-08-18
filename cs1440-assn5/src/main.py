#!/usr/bin/env python3  	    	       


#                         _  	    	       
#                        (o)<  DuckieCorp Software License  	    	       
#                   .____//  	    	       
#                    \ <' )   Copyright (c) 2022 Erik Falor  	    	       
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	    	       
#  	    	       
# Permission is granted, to any person who is EITHER an employee OR  	    	       
# customer of DuckieCorp, to deal in the Software without restriction,  	    	       
# including without limitation the rights to use, copy, modify, merge,  	    	       
# publish, distribute, sublicense, and/or sell copies of the Software, and to  	    	       
# permit persons to whom the Software is furnished to do so, subject to the  	    	       
# following conditions:  	    	       
#  	    	       
# The above copyright notice and this permission notice shall be included in  	    	       
# all copies or substantial portions of the Software.  	    	       
#  	    	       
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  	    	       
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  	    	       
# FITNESS FOR A PARTICULAR PURPOSE, EDUCATIONAL VALUE AND NONINFRINGEMENT. IN  	    	       
# NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,  	    	       
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR  	    	       
# OTHERWISE, ARISING FROM INDIGNATION, INDIGESTION, INDIFFERENCE, INDECENCY,  	    	       
# INDENTATION, INDETERMINATION, INTOXICATION, INDOCTRINATION, INTOLERANCE,  	    	       
# INDULGENCE, INDELICATENESS, INDISCRETION, INEFFECTIVENESS OR IN CONNECTION  	    	       
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

Deals with the command-line arguments

Issues a usage message when incorrect arguments are given

"""

import sys
import FractalParser
from FractalFactory import makeFractal
from PaletteFactory import makePalette
from ImagePainter import ImagePainter


palettes = [
    "ocean",
    "sunset",
    "forest"
]

defaultArguments = {
        'type': 'mandelbrot',
        'pixels': 640,
        'axislength': 0.00198413675654471,
        'iterations': 256,
        'min': {
            'x': -0.95524696837827,
            'y': 0.25543323162173
        },
        'max': {
            'x': -0.95326283162173,
            'y': 0.25741736837827
        },
        'pixelsize': 0.0000031002136820938,
        'imagename': 'blue-dragon'
}


isPalette = False

# quit when too many arguments are given
if len(sys.argv) > 3:
    print('Too many arguments given. Please give arguments as so:\n[FRACTAL_FILE [PALETTE_NAME]]')
    sys.exit(1)

elif len(sys.argv) == 1:
    # Creates a Default Fractal and Palette
    fractal = makeFractal(defaultArguments)
    palette = makePalette(defaultArguments['iterations'])
    image = ImagePainter(fractal, palette, defaultArguments)
    image.create_image()

# Check for a color palette
elif len(sys.argv) == 3:

    if sys.argv[2].lower() not in palettes:
        print("ERROR:", sys.argv[2], "is not a valid palette\nPlease choose one of the following:")
        for palette in palettes:
            print(palette)
        sys.exit(1)
    else:
        isPalette = True


# Use FractalParser to create a dictionary.
# Open the file and pass it to FractalParser to create a dictionary.
file = open(sys.argv[1])
fractal_info = FractalParser.parse(file, sys.argv[1])
file.close()

# Calls the FractalFactory and PaletteFactory functions
fractal = makeFractal(fractal_info)
palette = makePalette(iterations=fractal_info['iterations'])
if isPalette:
    palette = makePalette(fractal_info['iterations'], sys.argv[2])
else:
    print("PaletteFactory: Creating default color palette")

# Creates the image and saves it.
image = ImagePainter(fractal, palette, fractal_info)
image.create_image()
