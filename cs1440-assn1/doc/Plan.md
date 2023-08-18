# Software Development Plan

# Phase 0: Requirements Specification *(10%)*

## **Deliver:**

*   A detailed written description of the problem this program aims to solve.
*   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.

## Documentation For This Phase

1. This program is trying to *decrypt* DuckieCrypt messages into plain English.
     - There is already a program provided that Encrypts messages into DuckieCrypt.
     - There are three lessons provided to help with gaining the background info necessary to code 
this decrypter.
     
2. The Decrypter must be able to take the first 95 printable ASCII characters and translate them into 
plain english.
     - Characterse that are not DuckieCrypt characters should be _skipped_ and produce no output.

3. Handle invalid file paths
     - The Decrypter needs to be able to safely exit and provide information on why the program quit.

### **Good Solution**
     * A good solution to this program would be one that acurrately decrypts DuckieCrypt messages 
into plain English. It woould be able to handle invalid file paths and skip over _invalid_ 
characters.
     * I have not used python since 2020 due to me serving a mission so I don't really remember how 
to do anything right now. It seems like a giant switch statement might be the best thing to use to 
decrypt characters as the default has the potential to change any invalid characters into "".
     * Hopefully the lesson on handling invalid file paths is useful... otherwise that is going to be 
a major challenge for me.

# Phase 1: System Analysis *(10%)*

## **Deliver:**

*   List all of the data that is used by the program, making note of where it comes from.
*   Explain what form the output will take.
*   Describe what algorithms and formulae will be used (but don't write them yet).

## Documentation For This Phase

# Functions

 function that takes a file and reads it if possible, it should return an error if the file 
doesn't work

 main(filePath) -> [strings] or error

 create a function  that uses the .readlines() method to get an array of lines.
 
 this function would then loop through the array and remove all invalid characteres after 
"decrypting them"

 decrypt(string): -> string

# Phase 2: Design *(30%)*

## **Deliver:**

*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.

## Documentation For This Phase

'''Python
def main([string]): void
    file = getFile(safeFile)
    string to decode = safeFile.read()
    stringToPrint = ""
    for each word in the string to decode
        add the word to the string to print if it is valid
    close the file

note: The below functions functionality will be used with 3 different functions with 
duckieDecrypter.  One for uppercase, one for lowercase, and one for special characters.

def decrypt(string): string
    if string == "x"
        decode "x"
        return "x"

# Phase 3: Implementation *(15%)*

## **Deliver:**

*   (More or less) working Python code in `src/`.
*   Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan
    *   If you have nothing of note in this section, **note that you had nothing to note here, do not leave it blank.**

## Documentation For This Phase

I found out that there are no switch statement in python so I had to change my method there to using if elif statements.

During this phase I used the strip option but forgot to "re-save" the string as the stripped string which took a little time to debug.

As of now, I can only read files as an absolute path and I don't understand why. I'm going to investigate further and write my results here.
* I'm unsure of what the problem is as of right now. I may redo the filePaths lesson to see if that helps me out. or use REPL to help me out.
* The absolute path is the **as of now** only way to do it. Sucks for the grader but hopefully we learn how to get files better in the future.


# Phase 4: Testing & Debugging *(30%)*

## **Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.

## Documentation For This Phase

* My convertToSpecialChar() function wasn't working as expected for a litte. I thought it might be because there was a faux duckieCrypt that was just '+' and causing my 
function to return nothing. However, when I was reading each line in the file I was only iterating through a single character at a time. Once I was iterating through the 
strings, seperated by whitespaces, the function didn't work again.  This is because I forgot to "re-save" shortened duckieCode when using the .strip() function. Once I 
fixed that the program worked fine.

* Another bug I am currently working with is that I have to type in an absolute filepath in order for my program to work. This takes a long time and is ineffective. I'm 
going to research and try to fix this.

* After doing research I found out that this is the best/only way to get a file. Hopefully we learn a better way in the future.

# Phase 5: Deployment *(5%)*

## **Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Review the project to ensure that all required files are present and in correct locations.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
    *   Run through your test cases to avoid nasty surprises.

## Documentation For This Phase

* I have pushed my project up to gitlab. Verified my final commit (idk if we have to write anything but I checked.)
* All the required files a present, I don't know if they are in their correct locations, but I have not changed where the files are located so they 
should be.
* I have run through all the test cases multiple times and the program works. That isn't to say that a bug can't or won't be found though. There's always 
some snickety thing that we programmers don't think about.

# Phase 6: Maintenance

## **Deliver:**

*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to
        *   anybody besides yourself?
        *   yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading
        *   your computer's hardware?
        *   the operating system?
        *   to the next version of Python?

## Documentation For This Phase

* I don't fully understand how reading files works. I make sure to close each file I open but, I'm not really sure what all this .access and .R_OK and other 
functionalities of os is.  I'm sure that learning more about these methods would help the file be less sloppily written.

* If a bug was reported in a few months, it would not take long to find the cause of it. My functions are organized well and there are comments describing what each chunk 
of code does. Hopefully that would help if a bug was reported.

* My documentation should make sense to others as well as myself in six months time.

* I think it would be pretty easy to add a new feature to this program. Maybe it could read some other ASCII characters that weren't included in the encryptor or 
something. That would be cool and not hard to update.

* This program should work after upgrading to a new version of python or a new os. I think I actually did upgrade my os during the course of this project haha.
