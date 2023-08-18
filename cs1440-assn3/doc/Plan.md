# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

### Requirements:
     A program that accepts a single argument in the command line. The argument should be a directory containing CSV files.

     From the directory the shell will open up a file 'area-title.csv' that is **Hard-Coded** into the program.

     Read files one line at a time (if the file is too big and you try to read everything in at once, the program will crash)
          (i): Keep track of FIPS areas that may be included in the report by using a dictionary.

     From the directory the shell will open up a file '2021.annual.singlefile.csv' that is **Hard-Coded** into the program.
          (i): Only one line of this file may be stored in memory at a time.
               (j): Not a good idea to use .read() or .readLines()

     From each of these files, the program will print off any relevant data that the customer wants and ignore the rest.

### Solution Ideas:
     A good solution would include a program that asks for a directory, checks the files in that directory and prints the wanted output.
     It would only read one line at a time and **optimally** use dictionaries so finding the data is faster.
     The program would most likely use a dictionary to keep track of important FIPS, etc.

### What I know how to do:
     I know how to ask the user to enter arguments and I assume a directory will be about the same as a file.
     I know how to read files one line at a time and I know how to store and retrieve things from a dictionary.
     I know how to check the first few elements of a string (FIPS) to see if it is something we want.

### Anticipated challenges:
     Not necessarily a challenge but... Taking the time to read through a lot of documentation to see how FIPS work as well as other important information that 
we will be extracting from the files.
     Making sure the program includes all the information it needs and ignores the info it doesn't need/tracking down FIPS and everything.



## Phase 1: System Analysis *(10%)*

#### Inputs:
     The input will be a directory, and then a file. Then a whole lot of data that needs to be organized and checked etc.
     
#### Outputs:
     The output of the program will be a lot of text. The text will be information that we want will not include info that we do not want.
     It will take the form as a list of strings or just a lot of strings.

### KEY FUNCTIONS
     * Take a directory and open files from it.
     * Read in a file one line at a time and check if the info is needed. Record the data if it is needed.
     * Print out the information that is wanted.

     * Functions:
          * bigData.py??? There are no functions already written in the starter code...
          * convertToDict. A function that converts the area-titles.csv into a dictionary.
               (i): Takes a file as input and outputs a dictionary of data.
          * collectInfo. A function that collects info from the 2020.annual.singlefile.csv and puts it in a report object
               (i): Takes a file in as input and creates a report object after sorted through the data.



## Phase 2: Design *(30%)*

#### bigData.py

* Asks for a **directory** and tries to open a hardcoded file-path based on the directory.
     * Opens the hard-coded file, area-titles.csv if possible and crashes otherwise.

* Once the area-titles.csv is opened, loop through the file and read the file one line at a time.
     * Get the FIPS data and store it in a dictionary.  [FIPCODE : Place]
     
* Try to open the 2020.annual.singlefile.csv file and crash if unable to.
     * If the file opens parse through it and store the data as a rpt object. **We might be storing multiple report objects, the file is huge and each FIPCODE 
has lots of data that needs to be reported**

* Final:
     * print the rpt object after adding all data that we need to it.


The only bad input would be an invalid directory, so I do not think there is much to test for.
This assignment actually seems a lot easier after taking the time to read everything and realize what we have to do here. We'll see if that stands true.



## Phase 3: Implementation *(15%)*

* Going through implementation I learned that doing a for line in file: loop automagically reads one line of 
a file at a time. I was reading a line in the loop as well and that caused it to skip every other line.

* Other than that one problem, everything went well. Although making sure I had the right type before 
typecasting was a bit tedious.

  

## Phase 4: Testing & Debugging *(30%)*

* Tested for a directory that did not have the files hardcoded in. The program crashed as expected. 
  ```
  python3 src/bigData.py src/Report.py
      Reading the databases...
      Traceback (most recent call last):
        File "src/bigData.py", line 185, in <module>
          fipAreas = getFIPS(filePath=sys.argv[1])
        File "src/bigData.py", line 37, in getFIPS
          f = open(filePath + "/area-titles.csv")
      NotADirectoryError: [Errno 20] Not a directory: 'src/Report.py/area-titles.csv'
  ```
  
* Tested to see if a usage error would be thrown if no directory was provided and there was one thrown.
```
python3 src/bigData.py              
Usage: src/bigData.py DATA_DIRECTORY
 Exactly one argument must be given.
 ```

* I have not tested this one, but a foreseeable problem would be a directory with an `area-titles.csv` file
that did not follow the standard conventions the program is expecting. The same would be true with 
a rogue `2021.annual.singlefile.csv` file. Test these cases in the future and perhaps through an error
letting the user know.



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

* The only part in my program that may be hard to understand is the function that creates a report object.
The code uses many if statements that check values in an array. If the next programmer was unfamiliar with 
the file the data is coming from it would be very hard to piece together.

* If a bug was reported within the next few months I do not believe it would take long to find. 
The program is pretty short and knowing where the bug most likely occured should be fairly easy.

* I believe the documentation should make sense to almost anybody reading it. I would understand it in 6 months time too.
* I feel it would be pretty easy to add a new feature in a year. The only feature I could think of adding is parsing through more data
and all that requires is checking for another object in the fileline array, which is not hard at all.
* This program should work if my computers hardware or the operating system was upgraded. Hopefully it would still work in the next version of python
I don't see them changing anything too drastic.
