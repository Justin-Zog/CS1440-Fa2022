# Bingo! User Manual

## Menu And Functionality

#### Main Menu
The Main Menu will look like this:

     Main Menu:
     C) Create a new deck
     X) Exit the program

     Enter a Main command (C, X)

This menu will give you a prompt where you can choose to either:

1. Create a deck by entering 'c' or 'C'.

2. Exit the Program by entering 'x' or 'X'.

Entering anything else will simply repeat the menu and let you know that your input was invalid.

#### Card Size Menu
This menu will ask you how big you want your Bingo cards to be.

This program allows you to make cards as small as 3x3 and as large as 16x16.

The card size menu will look like this:

     Please input a number in the range [3 - 16]

     Enter card size [3 - 16]:

You can do this by entering a number between 3 and 16.

Entering anything outside this range will simply repeat the menu and let you know that your input was invalid.

#### Max Value Menu
This menu will ask you to choose the maximum value you would be okay with appearing on a Bingo card.

The Max Value Menu will look like this:

     Enter max number [x - m]:

In this menu you can enter a number between x and m.

Entering anything outside this range will simply repeat the menu and let you know that your input was invalid.

#### Deck Size Menu
This menu will ask you how many cards you want to be in your deck.

The Deck Size Menu will look like this:

     Enter number of cards [2 - 8192]:

You can enter a number between 2 and 8192. This will make a deck as small as 2 cards and as large as 8,192 cards.

Entering anything outside this range will simply repeat the menu and let you know that your input was invalid.

#### Deck Menu
The Deck Menu will look like this:

     Deck Menu:
     P) Print a card to the screen
     D) Display the whole deck to the screen
     S) Save the whole deck to a file
     X) Return to the Main menu

     Enter a Deck command (P, D, S, X)

You can enter the letters 'P', 'D', 'S', or 'X'.

Entering 'P' will bring you to a new menu that will ask you which card you want printed to the screen.

Entering 'D' will print the entire deck to the screen. Then display the Deck Menu again.

Entering 'S' will prompt you to enter a filename, then save the whole deck to that file.

Entering 'X' will bring you back to the Main menu and erase the Deck of Bingo cards.

Entering anything else will simply repeat the menu and let you know that your input was invalid.

#### Display Card Menu:
This menu will ask you which card you want to be printed to the screen.

The Display Card Menu will look like this:

     ID of card to print [1 - m]:

You may enter a number as low as 1 and as high as 'm'.

Entering a number outside this range will repeat the menu.

#### Save Deck Menu:
This menu will ask you where you want to save your Bingo Deck to.

The Save Deck Menu will look like this:

     Enter a filepath to save the deck to:

You may enter any valid filepath here.

## Common Errors and How to Fix Them

Common errors are entering invalid input into the menus.
The program will tell you what input you may enter, 
if you enter an invalid input, the program will let you know and display the menu again.

