# Justin Herzog A02306067 Was Here.

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
asks for file objects as input
               * each file is opened one at a time
               * lines are printed one at a time
               * don't print extra blank lines between lines
               * **close the file after using it**
"""

from Usage import usage


def cat(args):
    """concatenate files and print on the standard output"""
    # Tell the user they need to put arguments in and the format in which they should do so.
    if len(args) == 0:
        # Lets the user know they need to put arguments and shows them how to use cat.
        usage(error="No arguments provided. Please enter a file to concatenate.", tool="cat")

    for file in args:
        f = open(file)
        for line in f:
            print(line, end="")
        f.close()


def tac(args):
    """concatenate and print files in reverse"""
    # Tell the user they need to put arguments in and the format in which they should do so.
    if len(args) == 0:
        # Lets the user know they need to put arguments and show them how to use tac.
        usage(error="No arguments provided. Please enter a file to tac.", tool="tac")

    # Assumes the arguments given were files, opens and prints them in reverse order.
    for file in args:
        f = open(file)
        fileLines = f.readlines()
        if fileLines == []:
            print(f"{file} is completely empty.")
        else:
            for line in reversed(fileLines):
                print(line, end="")

        f.close()
