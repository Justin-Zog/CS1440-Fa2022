# Justin Herzog A02306067

#!/usr/bin/env python
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


# Feel free to start from scratch, or repurpouse any of these suggested  	    	       
#   functions! The world is yours. Well, maybe that was a bit of an over  	    	       
#   exaggeration... The world isn't only *yours*, but this file sure is.  	    	       
# Okay, I actually lied. Please keep the stuff management asks you to at the  	    	       
#   bottom of the file, in the if __name__ == "__main__": block.  	    	       

import sys  	    	       
from os import getcwd
from os import access
from os import R_OK


def sendError(msg=None, exitCode=1):
    '''  	    	       
DESCRIPTION:  	    	       
  Exits the program after printing an error message.

PARAMETERS:  	    	       
  msg : None | str  	    	       
    The message to print in the error message.  	    	       
    If no `msg` is given, the default message becomes "Error! An error was  	    	       
        encountered, so the program is quitting."  	    	       
  exitCode : int  	    	       
    The exit code to exit the program with.  	    	       
    If no exitCode argument is given, it defaults to 1.  	    	       

RETURNS:  	    	       
  Nothing, program quits with exit code `exitCode`  	    	       
    '''  	    	       
    # Dear Future Dev,  	    	       
    # The code below is fine. Your work is not needed on `sendError`.  	    	       
    # You are more than welcome to edit the string literal, especially to make  	    	       
    # a more vocal and unique quack.  	    	       
    if msg is None:  	    	       
        msg = "ERROR! An error was encountered, so the program is quitting."  	    	       
    print(f"""\  	    	       
!!!QUACK QUACK!!!  	    	       
================================================================================  	    	       
{msg}  	    	       
================================================================================  	    	       
!!!QUACK QUACK!!!  	    	       
""")  	    	       
    sys.exit(exitCode)  	    	       

def convertToLower(charCode):
    # Ensures that there is actual content after the '_'
    if len(charCode) == 1:
        return ""
    # We need to take the duckieCrypt, convert it to its ord() value, then use chr() to get it to the letter it is.
    startingOrd = ord("a")
    # Convert the charCode to a normal letter
    duckieNumber = charCode.strip("_")
    if duckieNumber.isdigit():
        # Ensures that the duckieNumber a letter between a and z
        if (int(duckieNumber) >= 0 and (int(duckieNumber)) <= 25):
            return chr((int(duckieNumber) + startingOrd))
        else:
            return ""
    else:
        return ""

def convertToUpper(charCode):
    # Ensures that there is actual content after the '^'
    if len(charCode) == 1:
        return ""
    # We need to take the duckieCrypt, convert it to its ord() value, then use chr() to get it to the letter it is.
    startingOrd = ord("A")
    # Convert the charCode to a normal letter
    duckieNumber = charCode.strip("^")
    if duckieNumber.isdigit():
        # Ensures that the duckieNumber a letter between A and Z
        if (int(duckieNumber) >= 0 and (int(duckieNumber)) <= 25):
            return chr((int(duckieNumber) + startingOrd))
        else:
            return ""
    else:
        return ""

def convertToSpecialChar(charCode):
    # Ensures that there is actual content after the '+'
    if len(charCode) == 1:
        return ""
    # Convert the charCode to just a letter and number
    duckieCode = charCode.strip("+")

    if duckieCode[0] == "A" and len(duckieCode) == 2 or len(duckieCode) == 3:
        duckieCode = duckieCode.strip("A")
        startingOrd = ord(" ")
        if duckieCode.isdigit():
            # Ensures that the duckieNumber a character between " " and @
            if (int(duckieCode) >= 0 and (int(duckieCode)) <= 32):
                return chr((int(duckieCode) + startingOrd))
            else:
                return ""
        else:
            return ""

    elif duckieCode[0] == "B" and len(duckieCode) == 2:
        duckieCode = duckieCode.strip("B")
        startingOrd = ord("[")
        if duckieCode.isdigit():
            # Ensures that the duckieNumber a character between [ and `
            if (int(duckieCode) >= 0 and (int(duckieCode)) <= 5):
                return chr((int(duckieCode) + startingOrd))
            else:
                return ""
        else:
            return ""

    elif duckieCode[0] == "C" and len(duckieCode) == 2:
        duckieCode = duckieCode.strip("C")
        startingOrd = ord("{")
        if duckieCode.isdigit():
            # Ensures that the duckieNumber a character between { and ~
            if (int(duckieCode) >= 0 and (int(duckieCode)) <= 3):
                return chr((int(duckieCode) + startingOrd))
            else:
                return ""
        else:
            return ""

    else:
        return ""

def decryptLine(line):
    output = ""
    lineArray = line.split()
    for duckieCrypt in lineArray:
        if duckieCrypt[0] == "^":
            output = (output + convertToUpper(duckieCrypt))
        elif duckieCrypt[0] == "_":
            output = (output + convertToLower(duckieCrypt))
        elif duckieCrypt[0] == "+":
            output = (output + convertToSpecialChar(duckieCrypt))
        else:
            # This is a faux duckieCrypt Character don't do anything to decrypt it.
            pass

    return output

def getFile(pathToFile):

    # Asks the user to enter a file again if nothing was entered.
    if pathToFile == "":
        pathToFile = input("Please select a text file to parse: ")

    if access(pathToFile, R_OK):
        # Creates a file object and opens it
        file = open(pathToFile)
        return file
    else:
        # Sends the user an error if the file cannot be accessed.
        sendError(msg=f"The provided file path {pathToFile} is not accessible")

    '''  	    	       
DESCRIPTION:  	    	       
  Checks the `pathToFile` that was given. If it exists, return a file object  	    	       
    for that file. Otherwise, exit the program with a message indicating the  	    	       
    issue.  	    	       

PARAMETERS:  	    	       
  pathToFile : str  	    	       
    The file path for the file that should be opened and decrypted  	    	       

RETURNS:  	    	       
  An opened file object OR quits program, not returning anything  	    	       
    '''


def main(filePath):  	    	       
    '''  	    	       
DESCRIPTION:  	    	       
  Run the main logic of the DuckieDecrypter program. Decrypts a given file, if  	    	       
    it exists, printing out the result.  	    	       

PARAMETERS:  	    	       
  filePath : str  	    	       
    The relative or absolute path to the file to decrypt  	    	       

RETURNS:  	    	       
  Nothing. Just prints out the decrypted text.  	    	       
    '''  	    	       
    ### MANAGEMENT COMMENT:  	    	       
    ###   This function is relied on in the code provided by management below.  	    	       
    ###   If you change this functions name or parameters, be sure to update  	    	       
    ###     the provided code below so it works.  	    	       
    file = getFile(filePath)  	    	       
    for line in file.readlines():  	    	       
        print(decryptLine(line))

    file.close()


# This block of code in the `if __name__ == "__main__":` block will *only* be  	    	       
#   executed if this duckieDecrypter.py file is run as the *main* file. Not if  	    	       
#    it's imported! It's the entry point to our program. Neat, right?  	    	       
# You'll probably see this in a lot of Python code out there.  	    	       

if __name__ == '__main__':  	    	       

    ### DUCKIECORP MANAGEMENT COMMENT:  	    	       
    ###   Do not modify the code after this comment, unless otherwise noted.  	    	       
    ###   The following code has been explained in the comments for you.  	    	       

    # The user asks for a help message by giving the argument '-h' or '--help'  	    	       
    if "-h" in sys.argv or "--help" in sys.argv:  	    	       
        # This is a block string used to make the error message  	    	       
        MSG = f"""\  	    	       
USAGE:  	    	       
  $ python {sys.argv[0]} [FILE PATH]  	    	       

DESCRIPTION:  	    	       
  The DuckieDecrypter is a proprietary tool created by DuckieCorp to *decrypt*  	    	       
    messages that are composed of DuckieCrypt. That is, to turn DuckieCrypt  	    	       
    back into plain text.  	    	       

ARGUMENTS:  	    	       
  [FILE PATH] : Optional  	    	       
    Specify the path to a file containing DuckieCrypt to decrypt.  	    	       
    If this argument is not given, then the user is prompted for manual input  	    	       
      for the file path.  	    	       
    Only one file can be specified.  	    	       

  -h | --help  	    	       
    Produce this help message if given as any argument to the program.  	    	       
"""  	    	       
        print(MSG, end='')  	    	       
        # Program quits here if the usage message is asked for  	    	       
        sys.exit(0)  	    	       
    # If the file path argument was given...  	    	       
    elif len(sys.argv) > 1:  	    	       
        # Extract the file path argument from the command line  	    	       
        filePath = sys.argv[1]  	    	       
    # No arguments were given...  	    	       
    else:  	    	       
        # So we manually prompt the user for the file  	    	       
        print(f"Your current working directory is:\n  {getcwd()}")  	    	       
        filePath = input("File to decrypt: ")  	    	       

    # Actually run the logic of the DuckieDecrypter by decrypting the file at  	    	       
    #   the location `filePath`  	    	       
    # You *can* modify this single line if you modify `main` above.  	    	       
    main(filePath)  	    	       
