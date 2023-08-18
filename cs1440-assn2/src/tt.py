#!/usr/bin/python3

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


import sys  	    	       

from Concatenate import cat, tac  	    	       
from CutPaste import cut, paste  	    	       
from Grep import grep  	    	       
from Partial import head, tail  	    	       
from Sorting import sort  	    	       
from WordCount import wc  	    	       
from Usage import usage  	    	       


if len(sys.argv) < 2:  	    	       
    usage()  	    	       
    sys.exit(1)  	    	       
else:
    # sys.argv >= 2 so we should check and see if the [1] element is one of our editors.
    # Gets all arguments that aren't tt.py and the argument after tt.py
    args = []
    for index in range(len(sys.argv)):
        if index > 1:
            args.append(sys.argv[index])

    # Checks which argument they invoked.
    if sys.argv[1] == "cat":
        cat(args=args)
    elif sys.argv[1] == "tac":
        tac(args=args)
    elif sys.argv[1] == "cut":
        cut(args=args)
    elif sys.argv[1] == "paste":
        paste(args=args)
    elif sys.argv[1] == "grep":
        grep(args=args)
    elif sys.argv[1] == "head":
        head(args=args)
    elif sys.argv[1] == "tail":
        tail(args=args)
    elif sys.argv[1] == "sort":
        sort(args=args)
    elif sys.argv[1] == "wc":
        wc(files=args)
    else:
        usage(error="The command you entered is not recognized.")

    # print("TODO: determine which tool the user has invoked") Checkmate
    # print("TODO: call on that tool, forwarding any remaining arguments to it") Checkmate