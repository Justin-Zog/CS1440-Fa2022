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

from math import floor  	    	       

from Deck import Deck
from Menu import Menu  	    	       
from MenuOption import MenuOption  	    	       


class UserInterface():  	    	       
    """  	    	       
    Provide the UserInterface for the program, which consists of the Main menu and the Deck menu  	    	       

    Also provides methods for accepting and validating user input  	    	       
    """  	    	       

    def __init__(self):  	    	       
        self.__m_currentDeck : Deck
        self.__m_menu = Menu("Main")  	    	       
        self.__m_menu += MenuOption("C", "Create a new deck")  	    	       
        self.__m_menu += MenuOption("X", "Exit the program")  	    	       

    def run(self):  	    	       
        """  	    	       
        Return None: present the main menu to the user  	    	       

        Repeatedly prompt for a valid command until good input is given, or the program is exited  	    	       
        """  	    	       

        print("""
 ########   ####  ##    ##   ######     #######   ####
 ##     ##   ##   ###   ##  ##    ##   ##     ##  ####
 ##     ##   ##   ####  ##  ##         ##     ##  ####
 ########    ##   ## ## ##  ##   ####  ##     ##   ##
 ##     ##   ##   ##  ####  ##    ##   ##     ##
 ##     ##   ##   ##   ###  ##    ##   ##     ##  ####
 ########   ####  ##    ##   ######     #######   ####

    Welcome to the DuckieCorp Bingo! Deck Generator""")  	    	       

        while True:  	    	       
            command = self.__m_menu.prompt()  	    	       
            if command.upper() == "C":  	    	       
                self.__create_deck()  	    	       
            elif command.upper() == "X":  	    	       
                break  	    	       

    def __create_deck(self):  	    	       
        """  	    	       
        Return None: Create a new Deck  	    	       

        The Deck is stored in self.__m_currentDeck  	    	       

        """

        card_size = 0
        max_num = 0
        deck_size = 0

        ### CARD SIZE MENU BEGINS HERE ###
        # I learned from a previous experience that no menu items need to be included in here.

        while True:
            print("Card Size Menu:\n"
                  "Please input a number in the range [3 - 16]\n\n"
                  "Enter card size [3 - 16]: ")

            command = input()
            if command.isdecimal():
                if 3 <= int(command) <= 16:
                    card_size = int(command)
                    break
                else:
                    print(f"'{command}' is not a valid option")
            else:
                print(f"'{command}' is not a valid option")


        ### MAX NUM MENU BEGINS HERE ###

        lower_bound = (2 * card_size * card_size)
        upper_bound = (floor(3.9 * card_size * card_size))

        while True:
            print("Max Value Menu:\n\n"
                  "Enter max number [{} - {}]".format(lower_bound, upper_bound))

            command = input()
            if command.isdecimal():
                if lower_bound <= int(command) <= upper_bound:
                    max_num = int(command)
                    break
                else:
                    print(f"'{command}' is not a valid option")
            else:
                print(f"'{command}' is not a valid option")


        ### DECK SIZE MENU BEGINS HERE ###

        while True:
            print("Deck Size Menu:\n"
                  "How many bingo cards would you like to make?\n\n"
                  "Enter number of cards [2 - 8192]: ")

            command = input()
            if command.isdecimal():
                if 2 <= int(command) <= 8192:
                    deck_size = int(command)
                    break
                else:
                    print(f"'{command}' is not a valid option")
            else:
                print(f"'{command}' is not a valid option")

        # Creates a deck
        self.__m_currentDeck = Deck(card_size=card_size, num_cards=deck_size, max_num=max_num)
        self.__deck_menu()


    def __deck_menu(self):
        """  	    	       
        Return None  	    	       

        Present the deck menu to user until a valid selection is chosen  	    	       
        """  	    	       
        menu = Menu("Deck")  	    	       
        menu += MenuOption("P", "Print a card to the screen")  	    	       
        menu += MenuOption("D", "Display the whole deck to the screen")  	    	       
        menu += MenuOption("S", "Save the whole deck to a file")  	    	       
        menu += MenuOption("X", "Return to the Main menu")  	    	       

        while True:  	    	       
            command = menu.prompt()  	    	       
            if command.upper() == "P":  	    	       
                self.__print_card()  	    	       
            elif command.upper() == "D":  	    	       
                print(self.__m_currentDeck.__str__())
            elif command.upper() == "S":  	    	       
                self.__save_deck()  	    	       
            elif command.upper() == "X":  	    	       
                break


    def __print_card(self):  	    	       
        """  	    	       
        Return None: Print one Card from the Deck  	    	       

        Prompt user for a Card ID  	    	       
        """  	    	       
        while True:
            # Ask for card, check if valid
            print("ID of card to print [{} - {}]".format(1, self.__m_currentDeck.__len__()))

            command = input()

            if command.isdecimal():
                if 1 <= int(command) <= self.__m_currentDeck.__len__():
                    print(self.__m_currentDeck.__getitem__(int(command) - 1))
                    break
                else:
                    print(f"'{command}' is not a valid option")
            else:
                print(f"'{command}' is not a valid option")

    def __save_deck(self):  	    	       
        """  	    	       
        Return None: Save a Deck to a file  	    	       

        Prompt user for the name of file to write the entire Deck into  	    	       
        """
        invalid_characters = "#%&{}\\<>*?$!'\":@+`|="


        print("Save Deck Menu:\n"
              "CAUTION: This could overwrite a file that already exists!\n"
              "Please make sure you do not enter a file that already exists unless you intend to replace that file.\n\n"
              "Where would you like to save your bingo cards to?\n")

        # It doesn't really matter what the user put in.
        # As long as it is a valid file name it should work.

        while True:

            command = input()
            b_valid_file = True
            for character in command:
                if character in invalid_characters:
                    b_valid_file = False

            if b_valid_file:
                # Save to the file and break.
                f = open(command, "w")
                f.write(self.__m_currentDeck.__str__())
                f.close()
                print("File Saved Successfully!")
                break

            else:
                print(f"{command} is not a valid file name. Your file cannot include any of the following characters:\n"
                      f"{invalid_characters}")
