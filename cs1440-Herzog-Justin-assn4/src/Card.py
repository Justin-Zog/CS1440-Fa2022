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

class Card():  	    	       
    COLUMN_NAMES = list("BINGOSKALEMDRUTZ")

    def __init__(self, idnum, number_set):
        """  	    	       
        Initialize a Bingo! card  	    	       
        """  	    	       
        self.__i_id = idnum
        self.__number_set = number_set

    def id(self):  	    	       
        """  	    	       
        Return an integer: the ID number of the card  	    	       
        """  	    	       
        return self.__i_id

    def get_number_set(self):
        """
        Return a number set
        """
        return self.__number_set

    def number_at(self, row, col):  	    	       
        """  	    	       
        Return an integer or a string: the value in the Bingo square at (row, col)  	    	       
        """  	    	       
        return self.__number_set[row][col]

    def __len__(self):
        """  	    	       
        Return an integer: the length of one dimension of the card.  	    	       
        For a 3x3 card return 3, for a 5x5 return 5, etc.  	    	       

        This method was called `size` in the C++ version  	    	       
        """  	    	       
        return len(self.__number_set[0])

    def __str__(self):  	    	       
        """  	    	       
        Return a string: a neatly formatted, square bingo card  	    	       

        This is basically equivalent to the `operator<<` method in the C++ version  	    	       
        """

        string_to_return = ""

        string_to_return += "Card #{}\n".format(self.id() + 1)
        # Print of the BINGO top part of the card
        for i in range(0, self.__len__()):
            string_to_return += f"   {self.COLUMN_NAMES[i]}  "

        string_to_return += "\n"

        row_tracker = 0
        # Print The Rest of the card
        for i in range(0, ((self.__len__() * 2) + 1)):
            column_tracker = 0
            string_to_print = ""
            for j in range(0, ((self.__len__() * 2) + 1)):
                if i % 2 == 0:
                    if j % 2 == 0:
                        string_to_print += "+"
                    else:
                        string_to_print += "-----"
                else:
                    if j % 2 == 0:
                        string_to_print += "|"
                    else:
                        if self.number_at(row_tracker, column_tracker) == self.__number_set[int(self.__len__() / 2)][int(self.__len__() / 2)] and self.__len__() % 2 != 0:
                            string_to_print += "FREE!".center(5)
                        else:
                            string_to_print += str(self.number_at(row_tracker, column_tracker)).center(5)

                        column_tracker += 1


            string_to_return += (string_to_print + "\n")
            if i % 2 != 0:
                row_tracker += 1

        return string_to_return
