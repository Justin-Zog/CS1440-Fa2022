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


def cut(args):
    """remove sections from each line of files"""
    fieldsToCut = []
    filesToCut = []
    moreThanOneField = False

    # Tell the user they need to put arguments in and the format in which they should do so.
    if len(args) == 0:
        # Lets the user know they need to put arguments and shows them how to use cut.
        usage(error="No arguments provided. Please enter the files you wish to cut.", tool="cut")

    if args[0] == "-f":
        # Removes '-f' from args
        args.pop(0)
        # Check to see that there are arguments after -f
        if len(args) < 1:
            usage(error="You need to add arguments after -f. ", tool="cut")

        # See what field(s) they want cut and put the field in order from least to greatest
        fieldsToCutArray = args[0].split(sep=",")
        for element in fieldsToCutArray:
            if element.isdigit():
                if int(element) > 0:
                    fieldsToCut.append(int(element))
                else:
                    usage(error="You entered an invalid field. Make sure the arguments after '-f' are comma seperated integers greater than 0.", tool="cut")
            else:
                usage(error="You entered an invalid field. Make sure the argument after '-f' is a comma seperated list of integeres greater than 0.", tool="cut")

        # Removes the wanted fields from args
        args.pop(0)
    else:
        fieldsToCut.append(1)

    # There should only be files at this point in the function
    if len(fieldsToCut) > 1:
        moreThanOneField = True
        fieldsToCut.sort()

    # Runs a loop once for each file in the args
    for file in args:
        # Opens one file then puts an array of lines in an array filesToCut = List[List[str]]
        f = open(file)
        fileLines = f.readlines()
        if fileLines == []:
            print(f"{file} is completely empty.")
        else:
            filesToCut.append(fileLines)
        f.close()

    for file in filesToCut:
        for line in file:
            lineArray = line.split(sep=",")

            for item in fieldsToCut:
                if item > len(lineArray):
                    # The index is out of the files range and should be skipped.
                    if not moreThanOneField:
                        print()
                    break
                else:
                    if moreThanOneField and item != fieldsToCut[-1]:
                        print(lineArray[item - 1], end=",")
                    else:
                        print(lineArray[item - 1].replace("\n", ""))


def paste(args):
    """merge lines of files"""
    # Tell the user they need to put arguments in and the format in which they should do so.
    if len(args) == 0:
        # Lets the user know they need to put arguments and shows them how to use paste.
        usage(error="No arguments provided. Please enter the files you wish to paste.", tool="paste")

    # Make a list of a list of file lines as strings.
    filesToPaste = []

    for file in args:
        f = open(file)
        fileLines = f.readlines()
        if fileLines == []:
            print(f"{file} is completely empty.")
        else:
            filesToPaste.append(fileLines)

        f.close()

    # max(filesToPaste) was being buggy so I had to write this.
    biggestArray = 0
    for array in filesToPaste:
        if len(array) > biggestArray:
            biggestArray = len(array)

    # Iterate over each file object as many times as the largest file
    for index in range(biggestArray):
        for file in filesToPaste:
            # Sets a boolean to see if a comma should be printed or not.
            lastFile = False
            if filesToPaste.index(file) == (len(filesToPaste) - 1):
                lastFile = True

            # Prints off the line without a newline at the end.
            if index < len(file):
                if lastFile:
                    print(file[index].replace("\n", ""), end="")
                else:
                    print(file[index].replace("\n", ""), end=",")
            else:
                if not lastFile:
                    print(end=",")

        print()
