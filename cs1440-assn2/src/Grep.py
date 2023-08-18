# Justin Herzog A02306067 Was Here

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

from Usage import usage


def grep(args):
    """print lines that match patterns"""

    invertMatching = False

    # Tell the user they need to put arguments in and the format in which they should do so.
    if len(args) == 0:
        # Lets the user know they need to put arguments and shows them how to use grep.
        usage(error="No arguments provided. Please enter a pattern and at least one valid filename.", tool="grep")

    if args[0] == "-v":
        invertMatching = True
        # Remove the -v argument now that it served its purpose
        args.pop(0)

        # Checks to see that there is a pattern and an alleged file.
        if len(args) < 2:
            usage(error="Please provide a pattern and at least one filename.", tool="grep")

        pattern = args.pop(0)
        for file in args:
            f = open(file)
            fileLines = f.readlines()
            if fileLines == []:
                print(f"{file} is completely empty.")
            else:
                for line in fileLines:
                    if pattern not in line:
                        print(line, end="")

            f.close()

    if not invertMatching:
        # -v is not here so the first arg is the pattern
        # checks to see that there is an alleged file after the pattern and throws an error if not.
        if len(args) < 2:
            usage(error="Please provide a pattern and at least one filename.", tool="grep")

        pattern = args.pop(0)
        # pattern is no longer in args and an error won't be thrown as long as the user entered a valid file.
        for file in args:
            f = open(file)
            fileLines = f.readlines()
            for line in fileLines:
                if pattern in line:
                    print(line, end="")

            f.close()
