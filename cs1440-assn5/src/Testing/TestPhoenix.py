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
from Phoenix import Phoenix


# autocmd BufWritePost <buffer> !python3 runTests.py
class TestPhoenix(unittest.TestCase):  	    	       
    def test_count(self):
        self.assertEqual(Phoenix.count(Phoenix(100, j_const=complex(0.5667, 0.0), p_const=complex(-0.5, 0.0)), complex_number=complex(0, 0)), 5)
        self.assertEqual(Phoenix.count(Phoenix(100, j_const=complex(0.5667, 0.0), p_const=complex(-0.5, 0.0)), complex_number=complex(0.5, 0.5)), 27)
        self.assertEqual(Phoenix.count(Phoenix(600, j_const=complex(0.5667, 0.0), p_const=complex(-0.5, 0.0)), complex_number=complex(-0.5, 0.5)), 27)
        self.assertEqual(Phoenix.count(Phoenix(1000, j_const=complex(0.5667, 0.0), p_const=complex(-0.5, 0.0)), complex_number=complex(-0.5, -0.5)), 4)
        self.assertEqual(Phoenix.count(Phoenix(427, j_const=complex(0.5667, 0.0), p_const=complex(-0.5, 0.0)), complex_number=complex(0.5, -0.5)), 4)
        self.assertEqual(Phoenix.count(Phoenix(100, j_const=complex(0.5667, 0.0), p_const=complex(-0.5, 0.0)), complex_number=complex(0.8, 0)), 99)


if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
