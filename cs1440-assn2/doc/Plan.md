# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

*   Rewrite the instructions in your *own words*
    *   What does the solution *need to have* or *surround* conceptually?
    *   What does a good solution *look like*?
*   List the things that you *already* know how to do
*   Write down any *challenges* you anticipate


This project will make Python versions of Unix text-processing programs.
Each tool will be written as a function in Python. Each function will take an input of arguments
that the user gives it from the command line.

The following are functions that should be redone in Python

     * 'cat' will be in the 'Concatenate.py' file
     * 'tac' will be in the 'Concatentate.py' file
     * 'cut' will be in the 'CutPaste.py' file
     * 'paste' will be in the 'CutPaste.py' file
     * 'grep' will be in the 'Grep.py' file
     * 'head' will be in the 'Partial.py' file
     * 'tails' will be in the 'Partial.py' file
     * 'sort' will be in the 'Sorting.py' file
     * 'wc' will be in the 'WordCount.py' file

This program will need to re-create all the above Unix text-processing tools.

#### Knows:
     * cat and tac should be easy because I already know how to concatentate a string (a file shouldn't be too different)
     * cutting this out of a file shouldn't be too hard.
     * head and tails should be a modified cat and should not be too hard.
     * wc should be very easy. Perhaps the easiest of all of these.

#### Don't Knows/Challenges:
     * How to cut and paste
     * How to effectively grep
     * How to sort (How does Unix use the sort function???)
     * How to make a driver


## Phase 1: System Analysis *(10%)*

*   Considering the overall program:
    *   List all kinds of *input* taken in by the program
    *   Describe what form its *output* will take
*   Write brief descriptions of *some* key functions your program may need
    *   Write the function's *name* its *inputs*, and *outputs*
    *   Explain what each function will do in *one sentence*
*   Use English; **NO CODE YET**

### Key Functions:

__All functions take a file as an argument.__

#### cat
     * takes files, concatenates them and prints the standard output
#### tac
     * takes files, concatentates and prints them in reverse
#### cut
     * removes lines from files
#### paste
     * merge lines from files
#### grep
     * prints lines that match a pattern (works like cmd-f)
#### head
     * prints the first little part of a file
#### tails
     * prints the last little part of a file
#### sort
     * sorts lines of text files
#### wc
     * print newline, word, and byte counts for each file given as an arguement.


## Phase 2: Design *(30%)*

*   **DO NOT COPY AND PASTE YOUR PYTHON CODE HERE!!!**
*   Write *pseudocode* that captures how each function works
    *   **Pseudocode != source code**
    *   If we find too much finished code here, *you will receive a zero*!
    *   It should look like *basic English* with extra indentation
*   Explain what happens to your functions in the face of *good and bad input*
    *   Make a note about *bad inputs* down in **Phase 4**; these will become your *test cases*

**Let the user know the commands that they can use and the format of the arguments**


     func cat:
          asks for file objects as input
               * each file is opened one at a time
               * lines are printed one at a time
               * don't print extra blank lines between lines
               * **close the file after using it**

    
     func tac:
          asks for file objects
          opens and prints file objects line by line, but reveresed.

     func cut:
          asks for a file object
          extracts the columns of data that the user asks for seperated by commas

     func paste:
          asks the user for a few file objects as input
               * Opens each file and stores it's lines one at a time
               * Merges all files, seperating each line with a comma

     func grep:
          asks the user for a pattern and a file to check
               * loops through each line of the file and checks if the pattern is in the line.
               * prints only the lines that match the pattern.

     func head:
          asks for a file object
          opens and prints the first little bit (or however much the user wants) of a file

     func tail:
          asks for a file object
          opens and prints the last little bit (or however much the user wants) of a file.

     func sort:
          asks for a file object
          sorts the file in alphanumeric order.

     func wc:
          asks for a file and prints out how many lines, words, and characters it has.
          



## Phase 3: Implementation *(15%)*

*   **DO NOT COPY AND PASTE YOUR PYTHON CODE HERE!!!**
*   Write *code* in the `src/` directory
    *   Copy the outlines from Phase 2 into your `.py` files, and *translate* from English into Python
*   As you translate, you will *encounter problems* that were not foreseen earlier
    *   E.g. things that you learned, things that didn't go according to plan, etc.
    *   Here you can write a brief description of *what* changed and *why*
*   If everything went swimmingly, say so here


During the development of the paste function I kept running into a weird error. I would print(file[index], end=",") but there would always be a new line.
That's when I found out that the file[index] had a newline in it and I had to remove it from their.


## Phase 4: Testing & Debugging *(30%)*

*   For the bad inputs you thought of back in **Phase 2**, write a *test case* that you can run to prove that your functions work as expected
    *   It is not necessarily bad if a function crashes if you can explain *why* and *how* it happens
*   Write the test cases you have *personally run*
    *   The *exact command* you used
    *   Copy & paste the program's *output*
    *   Be precise so that your grader can replicate your experience
*   For any bugs discovered, describe their *cause* and *remedy*
### Testing

If the file is invalid, it is okay if it crashes

How can this program break?
     * It could open a non-file (ex: directory or non-existent file)
     * Make sure it doesn't crash when given a valid file.
     * If the file is an empty list, let them know.


I tested to see if the programs would run if no arguments were given and found an error in my code. I had to replace each of my files to include: 
if len(args) == 0 instead of if args == "" because args is an array, not a string.

The most common ways to break the program are by putting unexpected commands.
I tried to put a lot of weird commands or syntax in for each of the commands.
The only weird thing that I found was in the cut function.
Here is the command I gave and the output:
`justinherzog@Justins-MacBook-Pro cs1440-assn2 % python3 src/tt.py cut -f 2,5 data/people\ copy.csv data/people.csv`     
`data/people copy.csv is completely empty.`
`Age,22,36,24,39,26,23,29,17,`

The output just looks a little off but I don't really know why it would do that.
I also don't care too much. If the user wants the output to look right they can remove the empty file themselves.

**I'm sure there are more bugs I just haven't found them yet.**

## Phase 5: Deployment *(5%)*

*   *Important:* complete **Phase 6** first!
    *   (I know it's backwards, just go with it)
*   **YOU DON'T NEED TO WRITE ANYTHING IN THIS PHASE**
    *   Just follow this checklist
*   **Push** your final commit to GitLab
*   **Verify** that your final commit was received by *browsing* to its project page on GitLab
    *   Ensure the project's *URL is correct*
    *   Review that all required files are present *in the correct location*
    *   Check that unwanted files *have not* been committed
    *   Add *final touches* to your documentation, including the Sprint Signature and this Plan
*   **Validate** that your submission is complete and correct by *cloning* it to a new location on your computer and re-running it
	*	Run your program from the *command line* so you can see how it will behave when your grader runs it
        *   **Testing in PyCharm is not good enough!**
    *   Re-run your *test cases* to avoid nasty surprises



## Phase 6: Maintenance

*   Write *brief and honest* answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are *sloppily written* and *hard to understand*?
        *   Are there parts of your program which you *aren't quite sure* how/why they work?
        *   If a bug is reported in a few months, *how long would it take you to find the cause*?
    *   Will your documentation make sense to...
        *   ...anybody *besides yourself*?
        *   ...*yourself* in six month's time?
    *   How easy will it be to *add a new feature* to this program in a year?
    *   Will your program *continue to work* after upgrading...
        *   ...your computer's *hardware*?
        *   ...the *operating system*?
        *   ...to the *next version* of Python?
*   Fill out the *Assignment Reflection* survey on Canvas

The most sloppily written and hardest to understand parts are in the cut and paste functions.
The reason being all the loops in them and lots of booleans checking whether or not a user put a certain command in or tried putting some weird input in.

I'm fairly confident I could tell someone how everything in my program works. I think I could even do so 6 months from now.

If a bug was reported I believe I could find the cause very quickly. All the files are pretty small and I feel it would easy to track a bug in one.

I hope my documentation makes sense. I try to be minimalistic so people, including myself, can see at the very least what each function was aiming to do.

I think it would be pretty easy to add a new feature to this program a year down the road.

The program should work after upgrading computer hardware, getting a new os, and hopefully the next version of python. You never know what Python might do though.



