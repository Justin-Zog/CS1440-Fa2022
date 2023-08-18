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


def wc(files):
    """print newline, word, and byte counts for each file"""
    # Tell the user they need to put arguments in and the format in which they should do so.
    if len(files) == 0:
        # Lets the user know they need to put arguments and shows them how to use wc.
        usage(error="No arguments provided. Please enter a valid file path.", tool="wc")

    totalNewlines = 0
    totalWordCount = 0
    totalByteCount = 0

    for file in files:
        # Initializes the data that will be printed later. This will be reset each time a new file is run.
        newlineCount = 0
        wordCount = 0
        byteCount = 0
        # Assumes the arguments given was a file.
        f = open(file)
        for line in f:
            newlineCount += 1
            wordArray = line.split()
            wordCount += len(wordArray)
            byteCount += len(line)

        print('{:>9}   {:>9}   {:>9}   {:<30}'.format(newlineCount, wordCount, byteCount, file))
        totalNewlines += newlineCount
        totalWordCount += wordCount
        totalByteCount += byteCount
        f.close()

    if len(files) > 1:
        print('{:>9}   {:>9}   {:>9}   {:<9}'.format(totalNewlines, totalWordCount, totalByteCount, "total"))
