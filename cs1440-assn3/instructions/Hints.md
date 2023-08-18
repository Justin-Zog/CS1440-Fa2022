# CS 1440 Assignment 3: Big Data Processing - Hints

## Students' advice from last semester

*   Don't overthink it. FIPS codes are easier than you think.
*   Don't overthink it until you have a working program.
*   Make sure you fully understand the CSV format of the files before you start.  Really take your time understanding the files and what they contain before starting.
*   The concept of this assignment is a lot simpler than it sounds. Take some time to identify what information is important and how you'll separate it. The readme and hints files are very helpful for understanding this one.
*   Take your time to learn how FIPS codes work early, and make sure you read the documentation early to know which FIPS codes to exclude.
*   Using Python's string methods is very important for this assignment.
*   REPL. REPL. REPL.
*   Read through all of the directions before even starting to code.  Write up and have a plan before you even start to code.  
*   Don't be in a rush to get through the `README.md` files and other documentation. They are very helpful, re-read them multiple times in order to fully understand the scope of the project and what needs to happen.
*   LOOK AT THE STARTER CODE!  If it's solved in the source code, don't solve it yourself. If I had read the source code I would have basically had my plan written for me.
*   Remember that even though fields start at 1, lists start at 0 in python.
*   Don't get overwhelmed in the beginning. Read everything that is provided to you carefully and slowly. The actual code you have to write isn't even 100 lines. It is a simple implementation if you can just get all the instructions processed in your head. 
*   Almost all of the information you need about the assignment is written down somewhere by the Professor: in `README.md`, `Hints.md`, the lecture notes, etc. Try to find find and read all of those before seeking outside help.
*   Go away from the computer if you're too frustrated. At some point you're not getting anywhere just fuming at the screen.
*   Pay a lot of attention to the data types you use, and how you take data out of the lines. 



## Erik's Hints

### Don't copy code from the previous assignment

*   While you should apply the **lessons** from the previous assignment to this
    one, don't go so far as to apply **source code** from the Text Tools
    straight into this program.
*   Your solution to this assignment should be 100% brand-new code.
    *   Students get themselves stuck when they try to force code written for
        the Text Tools into this program.


### Cite external sources in your Software Development Plan

*   While you may discuss aspects of your program's high-level design with your
    study buddies, you must write your code independently.
*   Keep track of documentation and websites that helped you along your way.
    *   In addition to being honest, links to those articles may come in handy
        later!


### Look for analogies

*   This program operates a bit like the `grep` text tool.  `grep` scans
    through a file line-by-line and only outputs lines that contain a pattern.
    This program will scan through a file line-by-line and only operate on
    lines that match certain criteria.
*   This program shares with the `cut` text tool the feature that it splits
    lines of text into lists using commas as delimiters.
*   This isn't a sly hint that you should copy & paste code from the previous
    assignment or import those modules into this program.  The similarities
    between this program and the last are not that great.  Rather, use the Text
    Tools program as an *inspiration*.


### Debugging

* Interactive debugging is difficult when your main loop executes ~3 million
  times.  Debug your program with smaller input files that are easier to
  understand.
* Print-statement and Wolf Fence debugging are good approaches when faced with
  mammoth data.
* If you want to add extra calls to `print()` for your own debugging purposes
  but not have it affect the grading system, be sure to send the output to
  standard error (`sys.stderr`).  You can see how to do this in `src/bigData.py`.


### Files and paths

*   Don't use backslashes `\` as directory separators; they don't work properly
    on all systems or in all situations.  Use the frontslash `/` instead.
*   Your program must work regardless of its current working directory (CWD).
*   Your program must be able to work with *any* directory name that can be
    supplied on the command line, even directories not included with the
    starter code.


### area-titles.csv

*   Read this file line-by-line. As you read it:
    *   Discard unwanted FIPS areas.
    *   Collect this data into a Python dictionary mapping FIPS codes to area
        titles.
*   FIPS area codes follow a simple pattern which makes it easy to exclude the
    national aggregate, statewide aggregate metropolitan and micropolitan
    areas.
*   While some FIPS area codes look like integers, it is best to always treat
    them as strings.
*   `area-titles.csv` contains 4,726 lines of text, of which the first is a CSV
    header line.  After discarding unwanted FIPS areas you will be left with
    3,463 FIPS areas.
*   Read the `help()` documentation for `str.split` to learn how to split each
    line of `area-titles.csv` into exactly two fields regardless of the number
    of commas it contains.
*   FIPS area codes follow a pattern.  You can easily identify FIPS areas that
    must be excluded from consideration solely by looking at the FIPS code.  If
    you consider the human-friendly area title, you're working too hard.


### 2021.annual.singlefile.csv

*   Read this file line-by-line. As you read it:
    *   Skip lines about FIPS areas which do not belong in the report.
    *   Skip lines about industries which do not belong in the report.
    *   Skip lines having ownership codes which do not belong in the report.
*   The layout of this CSV file is described by
    [this document](https://data.bls.gov/cew/doc/layouts/csv_annual_layout.htm).
    Bear in mind as you read this document that we are using the **singlefile**.
*   Keep track of the data required for the report.  You must accumulate totals
    keep maximum values across three categories *and* keep track of the
    highest-ranked FIPS area.
*   This is a very big file and your program will take a long time to read it
    (my implementation takes ~6.5 seconds to read the file once on my laptop).
    Minimize the number of times your program reads the file.  One pass is
    enough.
*   Make sure that you have a program that *works* before you worry about
    having a program that is *fast*.

> Programmers waste enormous amounts of time thinking about, or worrying about,
> the speed of noncritical parts of their programs, and these attempts at
> efficiency actually have a strong negative impact when debugging and
> maintenance are considered. We should forget about small efficiencies, say
> about 97% of the time: premature optimization is the root of all evil. Yet we
> should not pass up our opportunities in that critical 3%.
> 
> – Donald Knuth
> "Structured Programming With Go To Statements"
> Computing Surveys, Vol 6, No 4, December 1974
