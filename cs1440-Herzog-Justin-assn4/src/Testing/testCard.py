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

from Card import Card  	    	       
from RandNumberSet import RandNumberSet  	    	       


class TestCard(unittest.TestCase):  	    	       

    def setUp(self):  	    	       
        """  	    	       
        Create no fewer than 5 Card objects to test  	    	       

        Create a mixture of odd and even-sized cards  	    	       
        """
        number_set_1 = RandNumberSet(nSize=5, nMax=63)
        number_set_1.shuffle()
        number_set_2 = RandNumberSet(nSize=16, nMax=785)
        number_set_2.shuffle()
        number_set_3 = RandNumberSet(nSize=3, nMax=18)
        number_set_3.shuffle()
        number_set_4 = RandNumberSet(nSize=9, nMax=236)
        number_set_4.shuffle()
        number_set_5 = RandNumberSet(nSize=8, nMax=173)
        number_set_5.shuffle()

        self.card1 = Card(idnum=1, number_set=number_set_1)
        self.card2 = Card(idnum=2, number_set=number_set_2)
        self.card3 = Card(idnum=3, number_set=number_set_3)
        self.card4 = Card(idnum=4, number_set=number_set_4)
        self.card5 = Card(idnum=5, number_set=number_set_5)


    def test_len(self):  	    	       
        """Assert that each card's size is as expected"""  	    	       
        self.assertEqual(len(self.card1), 5)
        self.assertEqual(len(self.card2), 16)
        self.assertEqual(len(self.card3), 3)
        self.assertEqual(len(self.card4), 9)
        self.assertEqual(len(self.card5), 8)

    def test_id(self):  	    	       
        """Assert that each card's ID number is as expected"""

        self.assertEqual(self.card1.id(), 1)
        self.assertEqual(self.card2.id(), 2)
        self.assertEqual(self.card3.id(), 3)
        self.assertEqual(self.card4.id(), 4)
        self.assertEqual(self.card5.id(), 5)


    def test_freeSquares(self):
        """  	    	       
        Ensure that odd-sized cards have 1 "Free!" square in the center  	    	       
        Also test that even-sized cards do not have a "Free!" square by examining the 2x2 region about their centers  	    	       
        """
        def has_free(s: str) -> bool:
            if "FREE!" in s:
                return True
            else:
                return False

        # Implementing this is going to be hard since I just print 'FREE!' if the card is odd and it's the middle square
        self.assertEqual(has_free(self.card1.__str__()), True)
        self.assertEqual(has_free(self.card2.__str__()), False)
        self.assertEqual(has_free(self.card3.__str__()), True)
        self.assertEqual(has_free(self.card4.__str__()), True)
        self.assertEqual(has_free(self.card5.__str__()), False)

    def test_no_duplicates(self):  	    	       
        """Ensure that Cards do not contain duplicate numbers"""
        def check_for_duplicates(a_list):
            # sets never have duplicates which is why this works
            if len(a_list) == len(set(a_list)):
                return False
            else:
                return True

        for i in range(len(self.card1)):
            self.assertEqual(check_for_duplicates(self.card1.get_number_set()[i]), False)

        for i in range(len(self.card2)):
            self.assertEqual(check_for_duplicates(self.card2.get_number_set()[i]), False)

        for i in range(len(self.card3)):
            self.assertEqual(check_for_duplicates(self.card3.get_number_set()[i]), False)

        for i in range(len(self.card4)):
            self.assertEqual(check_for_duplicates(self.card4.get_number_set()[i]), False)

        for i in range(len(self.card5)):
            self.assertEqual(check_for_duplicates(self.card5.get_number_set()[i]), False)


if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
