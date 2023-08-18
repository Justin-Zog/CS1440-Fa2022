# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

#### Problem
* We want to make a `d` sized deck of `n`x`n` bingo cards. Where 2 < `n` < 17.
     * `n` is given by the user as input in a menu. 2 < `n` < 17
     * `d` is given by the user as input in a menu. 1 < `d` < 8193.
     * `m` is given by the user as input in a menu. $[ 2 * n^2 \ldots floor(3.9 * n^2) ]$ 
##### Sub-Problems
* Odd sized `n` need to have a 'FREE!' square in the middle while even sized cards have **no** 'FREE!' square.
* Every card has a unique integer identifier

### Good Solution
A good solution to this problem would look like a user-friendly menu that makes
bingo cards as the user asks it to. It would allow the user to add these bingo cards to a file.

I am pretty sure I know how to do everything except for maybe writing the deck to a file.
I do not see any challenges in the future. There is bound to be at least 1 though, most likely more haha.


## Phase 1: System Analysis *(10%)*

#### Input

`n` : Given by the user, used to determine how big to make a card.

`d` : Given by the user, used to determine how big to make a deck.

`m` : Given by the user, used to determine the maximum integer the user wants to be on a 'bingo' card.

other menu entries given by the user will need to be verified.

**User Input Throughout** We don't know what the user may try to throw at us so we gotta check if they put in something valid.

#### Output
* Menus and prompts
* Bingo Cards


#### Algorithms and formulae
* Something that prints a bingo card correctly.
     * Numbers are not repeated
     * The piping looks good
     * etc.
* Something that creates a bingo card correctly.
     * The hardest part will most likely be making sure the card contains non-overlapping ranges
        of numbers. I think we can just loop through an array between two point tho.
* Something that displays the menu again if the user messed up.


## Phase 2: Design *(30%)*

**Deliver:**

*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.

### `MenuOption` class

Represents a part of a menu.  A `MenuOption` consists of a character that the user inputs to select it, and a string that gives a full description of what the option means in the program.

When a `MenuOption` object is printed, it displays like this: `A) This is option A`.

The `MenuOption` constructor will take two parameters: the character and description string.


### `Menu` class

This class contains a collection of `MenuOption` objects.  In order to keep the constructor simple, these options will be added/appended to this collection after the `Menu` object is instantiated.  A `Menu` will have a title or header (string) to indicate the purpose of the menu.

The `Menu` will act similar to an array. This will allow for ease of access to the MenuOptions that a Menu contains.

This object also has a `prompt()` operation, which displays the menu and awaits user input. Once the user has entered input, it will be checked to see if it is contained within any of the `MenuOptions`. If it is contained, the program will proceed. If it is not contained, the menu will be repeated forever until the user enters valid input.


### `UserInterface` class

This class ties all the other Classes together to make a coherent program.

There will be only one `UserInterface` object at a time in the program.

Initially, it will print the program logo and present the main `Menu`.  From the main menu the user can exit the program, or proceed to create a Deck. When the user chooses to proceed, the `Deck` creation menu is created and presented.  The `UserInterface` will then hold on to the `Deck` object until the user returns back to the main `Menu`; at that time the `Deck` is discarded.

This class also contains private methods that facilitate input/output for the user.

*   `string get_str(string prompt)` - Prompt the user with a `prompt`, then collect their input.  Return the `string` the user typed
*   `int get_int(string prompt, int lo, int hi)` - Prompt the user with a `prompt`, then collect their input.  If the input is not numeric, show the prompt again.  Repeat the prompt if the input is an integer but less than `lo` or greater than `hi`.
*   `create_deck()` - Guide the user through the questions that constrain how they create a Deck of Bingo Cards.
    *   Specifically, the user is asked for
        *   Size of Card $[ 3 \ldots 16 ]$ (use `get_int`)
        *   Max number to appear on Card $[ 2 * N^2 \ldots floor(3.9 * N^2) ]$ (use `get_int`)
        *   Size of Deck $[ 2 \ldots 8192 ]$ (use `get_int`)
*   `print_card()` - Prompt the user for a `Card` ID number to print.
    *   Use `get_int`
    *   Check that input is not greater than number of Cards in Deck
*   `save_deck()` - Prompt the user for a filename in which to save the current `Deck`.
    *   Uses `get_str` to ask the user for a filename
    *   The requirements don't ask us to validate the user's input - just trust that they know what they're doing and crash if something goes wrong.
    *   Printing a `Deck` to a file is pretty much the same as printing it to the screen.


### `RandNumberSet` class

The requirements for Cards are strict and require careful consideration to get right.  After going back and forth on this, it has been decided to keep the Bingo Card as simple as possible by treating it as a simple 2D array of numbers.  The complex logic needed to fill it in correctly will be sequestered into this class.

One requirement on `Card`s is that no number can be duplicated on a `Card`.  The most elegant solution we can come up with is to make one list of numbers running from 1 to the maximum number on the `Card`, and to shuffle it like a deck of cards, then draw numbers from the top until the Bingo `Card` is filled.  This requirement only holds within one `Card`: it is okay if the same number is shared among `Card`s within the `Deck`.

There is a requirement that numbers within columns of the Bingo `Card` be drawn from increasing subsets of numbers such that the leftmost column contains the smallest numbers, and increase toward the right side of the `Card`.  These subsets cannot overlap.  This seemed difficult at first, but is easily solved by dividing the `Card` into $N$ segments, and applying the "shuffle a set of numbers" idea to each segment individually.

*   Thus, the `RandNumberSet` will support a public `shuffle` operation which shuffles each segment and resets the object so that a new `Card` can be created.
    *   Reusing the object will conserve resources in the computer
*   Numbers for an entire row of a `Card` will be provided by the public `next_row()` method.
    *   The `RandNumberSet` will have a private data member `nRowPos` which keeps track of which row is the next to be returned by `next_row()`
*   The `RandNumberSet` constructor will need to know the size of `Card` it is being used to create (so it can know how many segments to divide its numbers into), as well as the maximum number that may appear on the card.
    *   This class relies on its caller to validate its input.
*   The `Card` size, maximum number and array of segments are stored in private members.
*   `__get_size__()` may be called to retrieve the maximum number size.
*   The size of the `RandomNumberSet` is defined to be the size of the `Card` it can create.  This value will be given by the public `size()` method.
*   `__str__()` prints the `RandomNumberSet`.


### `Deck` class

This class is essentially a container of `Card` objects (kinda like real life!).  Will possibly use a plain array, since the size of the `Deck` is known at the time of initialization.

The constructor will create each `Card` it will contain.  It will initialize a `RandNumberSet` to help with this process.  The constructor will take these parameters:

*   `int card_size` - the size of a `Card`, from 3 to 16
*   `int num_cards` - number of cards in the `Deck`, from 2 to 8192
*   `int max_num` - the highest number that may appear on a card, needed by the `RandNumberSet`

The usual assortment of public methods/overloads will be provided:

*   `size()` returns the number of `Cards` contained within
*   `__getitem__` returns a specific `Card`
*   `__string__` prints each `Card` in the `Deck`.  This method will rely on the `Card` object also overloading `__string__`


### `Card` class

This object will have private data members to hold:

*   `int id` - the `Card`'s ID number, needed when it prints itself out
*   `int size` - the number of rows in the `Card`, needed when determining whether the center square is **Free**
*   `int rows[][]` - the 2D array that holds on the numbers
    *   The **Free** square will contain a negative value; when the Card is printed the string `"FREE!"` will be printed instead.

All of the interesting work of instantiating this object is handled by the `RandNumberSet`.  The algorithm for creating the card goes like this:

```
0.  Shuffle the RandNumberSet to ensure that fresh numbers are at the top
1.  Until the card is full
    *   Grab the next row of numbers from the RandNumberSet
    *   Copy into the Card
2.  If the size of the Card is odd, replace the center square with the value `-1` to represent **Free**
```

*   A public `id()` method provides read-only access to the private `id` member
*   `number_at(row, col)` returns the number stored at cell `(row, col)`

The usual assortment of public methods/overloads will be provided:

*   `__len__` returns the size of the `Card`
*   `__str__` prints the `Card`.
    *   The ID # of the card is displayed above the `Card` itself
    *   ASCII-art rows and columns are drawn with dashes `-`, plus signs `+` and pipes `|`, according to the requirements
    *   Each number is centered within its cell
    *   It is easy to print the card to the screen or to a file.

## Phase 3: Implementation *(15%)*

**Deliver:**

During the implementation of this project, I changed the way a "FREE!" space was found.
The program instead checks to see if the card is odd and just prints "FREE!" instead of the number in the middle spot.
I changed this just because it was easier to do.

I also deleted a few of the methods contained within the Deck class. I never needed to use them.

Those are the only changes from the plan as far as I can remember.


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

#### Invalid Input Checks:


     Main menu:
        C) Create a new deck
        X) Exit the program

    Enter a Main command (C, X)
    a
    'a' is not a valid option

'

    Card Size Menu:
        Please input a number in the range [3 - 16]

        Enter card size [3 - 16]: 
        18
        '18' is not a valid option

'

    Max Value Menu:

    Enter max number [392 - 764]
    B14z3
    'B14z3' is not a valid option
    Max Value Menu:

    Enter max number [392 - 764]
    765
    '765' is not a valid option

'

    Deck Size Menu:
    How many bingo cards would you like to make?

    Enter number of cards [2 - 8192]: 
    ABE_LINCOLN_LIVES.txt            
    'ABE_LINCOLN_LIVES.txt' is not a valid option
    Deck Size Menu:
    How many bingo cards would you like to make?

    Enter number of cards [2 - 8192]: 
    1
    '1' is not a valid option

'

    Deck menu:
    P) Print a card to the screen
    D) Display the whole deck to the screen
    S) Save the whole deck to a file
    X) Return to the Main menu

    Enter a Deck command (P, D, S, X)
    PrettyPagliakSnigdrin
    'PrettyPagliakSnigdrin' is not a valid option

'

    ID of card to print [1 - 234]
    3456
    '3456' is not a valid option

'
    
    Save Deck Menu:
    CAUTION: This could overwrite a file that already exists!
    Please make sure you do not enter a file that already exists unless you intend to replace that file.

    Where would you like to save your bingo cards to?

    $hell$h@wk15.pdf
    $hell$h@wk15.pdf is not a valid file name. Your file cannot include any of the following characters:
    #%&{}\<>*?$!'":@+`|=

'

    Save Deck Menu:
    CAUTION: This could overwrite a file that already exists!
    Please make sure you do not enter a file that already exists unless you intend to replace that file.

    Where would you like to save your bingo cards to?

    B1gHa110w33nL0veR.onion
    File Saved Successfully!

## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 6: Maintenance

**Deliver:**

A few of the methods in Card.py are sloppily written and may cause some confusion.
When I first started coding I forgot the if the __len__ or __str__ functions are defined you can just call
len(object) and it will return whatever the __len__ function returns.
Because of that there are places in my code that call self.__len__() which looks bad to say the least.

I know why everything in the programs works and why they work. If a bug was reported I do not believe 
it would take very long to find the cause and fix it. 
I was able to understand my code when I looked at it after a few days. So it is fairly easy to understand. 

I think the documentation will be helpful to both myself and anyone else in 6 months. 
It is very explicit and goes into lots of details.

Adding a new feature in a year or so should be fairly easy because of the modular way this program is coded.
The program should keep working in the future too.



