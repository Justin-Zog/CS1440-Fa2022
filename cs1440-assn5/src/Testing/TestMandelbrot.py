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

import unittest
from Mandelbrot import Mandelbrot


# autocmd BufWritePost <buffer> !python3 runTests.py
class TestMandelbrot(unittest.TestCase):

    def test_count(self):
        self.assertEqual(Mandelbrot.count(Mandelbrot(100), complex_number=complex(-0.75, 1)), 2)
        self.assertEqual(Mandelbrot.count(Mandelbrot(100), complex_number=complex(-0.75, 0.1)), 32)
        self.assertEqual(Mandelbrot.count(Mandelbrot(330), complex_number=complex(-0.75, 0.01)), 314)
        self.assertEqual(Mandelbrot.count(Mandelbrot(100), complex_number=complex(0.25, 1)), 3)
        self.assertEqual(Mandelbrot.count(Mandelbrot(256), complex_number=complex(0.25, 0.01)), 255)
        self.assertEqual(Mandelbrot.count(Mandelbrot(330), complex_number=complex(0.25, 0.0001)), 329)


if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
