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

from Usage import usage


def head(args):  	    	       
    """output the first part of files"""
    # Tell the user they need to put arguments in and the format in which they should do so.
    if len(args) == 0:
        # Lets the user know they need to put arguments and shows them how to use head.
        usage(error="No arguments provided. Please enter a valid file to show.", tool="head")

    # The first argument will be the lines to print and the second will be the file to print.
    # Unless the user wants to use the default amount which I guess is 10 lines.
    if args[0] == "-n" and args[1].isdigit():
        # Removes '-n'
        args.pop(0)
        # Gets the int value of the lines they want printed
        linesToPrint = int(args.pop(0))
    elif args[0] == "-n" and not args[1].isdigit():
        usage(error="Number of lines required.", tool="head")
    else:
        linesToPrint = 10

    # There should be only files left if the user put in the arguments correctly.
    moreThanOneFile = False
    if len(args) > 1:
        moreThanOneFile = True

    for file in args:
        f = open(file)
        loopCounter = 0

        if moreThanOneFile:
            print(f"==> {file} <==")

        for line in f:
            if loopCounter < linesToPrint:
                print(line, end="")
                loopCounter += 1
            else:
                # Stops the loop once the right amount of lines is printed
                if moreThanOneFile:
                    print("")
                break

        f.close()

def tail(args):
    """output the last part of files"""
    # Tell the user they need to put arguments in and the format in which they should do so.
    if len(args) == 0:
        # Lets the user know they need to put arguments and shows them how to use tail.
        usage(error="No arguments provided. Please enter a valid file to show.", tool="tail")

    # The first argument will be the lines to print and the second will be the file to print.
    # Unless the user wants to use the default amount which I guess is 10 lines.
    if args[0] == "-n" and args[1].isdigit():
        # Removes '-n'
        args.pop(0)
        # Gets the int value of the lines they want printed
        linesToPrint = int(args.pop(0))
    elif args[0] == "-n" and not args[1].isdigit():
        usage(error="Number of lines required.", tool="tail")
    else:
        linesToPrint = 10

    # There should be only files left if the user put in the arguments correctly.
    moreThanOneFile = False
    if len(args) > 1:
        moreThanOneFile = True

    for file in args:
        f = open(file)
        fileLines = f.readlines()
        if fileLines == []:
            print(f"{file} is completely empty.")

        loopCounter = -linesToPrint

        if moreThanOneFile:
            print(f"==> {file} <==")

        if abs(loopCounter) > len(fileLines):
            loopCounter = -len(fileLines)

        for index in range(len(fileLines)):
            if loopCounter != 0:
                print(fileLines[loopCounter], end="")
                loopCounter += 1
            else:
                # Stops the loop once the right amount of lines is printed
                if moreThanOneFile:
                    print("")
                break

        f.close()
