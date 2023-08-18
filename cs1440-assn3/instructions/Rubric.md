# CS 1440 Assignment 3: Big Data Processing - Rubric

| Points | Criteria
|:------:|--------------------------------------------------------------------------------
| 10     | Shell Tutor lessons complete<br/>`shell-tutor/certificate.txt` file is present
| 25     | Software Development Plan is complete, comprehensive, well-written and follows DuckieCorp conventions
| 5      | Signature File is complete
| 10     | User interface/CLI meets requirements
| 15     | area-titles.csv is processed according to requirements <br/> The file is read one line at a time <br/> FIPS areas are included/excluded appropriately <br/>A built-in data structure is used to hold information about valid FIPS areas
| 25     | 2021.annual.singlefile.csv is processed according to requirements <br/>The file is read and processed one line at a time <br/> Only one line of the file is kept in memory at once <br/>Lines are skipped appropriately based on FIPS, industry and ownership codes <br/>Proper data conversion functions are employed
| 10     | Report output meets customer's requirements <br/>Program output matches provided examples <br/>Information is placed into the correct sections of the report <br/>Correct counts and totals are provided <br/>FIPS areas are displayed as "County, State" and not as FIPS codes

**Total points: 100**


## Penalties

*Please read the "How To Submit Assignments" page of Canvas (found under the DuckieCorp Employee Handbook Module) for more information on these penalties and what we expect.*

**_Penalties for this assignment_**:

0.  **100% point penalty** if your program imports any modules **except**:
    *   `sys`
    *   `typing`
    *   `time`
    *   `Report`
    *   or modules you wrote yourself
    *   This assignment is about the experience of solving this puzzle for yourself without leaning on code written by others, no matter how "real-world" it would be to do so.
1. **1 point penalty** per megabyte of CSV or ZIP files in your repository (`area-titles.csv` excepted).  If you accidentally commit a huge CSV file, ask the instructor for help.
2. **2 point penalty** per line of output on `sys.stdout` that is not due to printing the `Report` object.  Extra output to `sys.stderr` is permitted.
3.  **10 point penalty** Your program *must* hard-code the filenames `area-titles.csv` and `2021.annual.singlefile.csv` exactly as given.  Do not rename these files on your computer or in your code as this will cause your program to fail when we grade it.
4. **10 point penalty** program interactively prompts user for input.  All input to this program comes from command-line arguments or from files.

**_Penalties for all assignments_**:

#### Project Layout
0.  **10 point penalty** if the repository does not follow the Git Repository Naming Convention
1. **10 point penalty** if the submitted project is not a clone of the starter code repository.
2.  **10 point penalty** if there is an omission of required files and directories (missing, renamed, or moved from their expected location)
3.  **10 point penalty** if there are forbidden files and directories in the submission
4.  **10 point penalty** if there is no `.gitignore` file (whether it is missing or corrupted)
5. **Late Penalty**:
    *   \<24hrs late : 75% point cap
    *   \>=24hrs & <48hrs : 50% point cap
    *   \>=48hours : no points will be given; submissions not allowed after 48hrs

#### Modules and Functions
0. **10 point penalty** if a module fails to import due to misspelling or incorrect capitalization.
1. **10 point penalty** if the program attempts to import a module from the `src.` package; this is the result of a PyCharm misconfiguration.
2. **10 point penalty** `eval()` or a similar function is used by your program; use type constructor functions such as `int()` and `float()` instead
3. **\<Varies\> point penalty** A library which the grader doesn't happen to have installed is imported; The resulting `ModuleNotFoundError` is treated as a crash and penalized accordingly
4. **up to 100% point penalty** A library not permitted by the instructions is used, but doesn't result in a crash

#### Files and Paths
0.  **10 point penalty** if the program contains hard-coded paths or otherwise does not function when run from *any* CWD.  (Note: names of modules in `import` statements do not count as "hard-coded").
1.  **10 point penalty** if one or more data files are not closed after being processed in *ordinary* situations.  In the event of an error your program will display an error message and immediately exit; in such cases you do not need to take special measures to close files because they will automatically be closed as your program exits.
2.  **100% point penalty** if external programs are called upon to do the work.  Our customer has hired you to create a pure-Python solution, not a shell script that relies on external programs.
    - Do not use `os.system()`, `subprocess`, `pipes` or similar functions and libraries
    - Write a pure Python solution, not a script that leverages external programs

#### All Else
0. **Crashing Code Penalty**:
    * *Reminder: it is your responsibility to test and ensure that your program works on the graders computer*
    *   Code that is crashing and cannot be quickly & easily fixed by the grader will receive a 0% point cap penalty on the implementation portion of the rubric (0 points on implementation)
    *   Code that is crashing and CAN be quickly & easily fixed by the grader (or is only crashing some of the time) will receive a 50% point cap penalty on the implementation portion of the rubric


### What about Python's standard `csv` module?

There is a Python module named `csv` for processing CSV data.  **You cannot use
it to complete this assignment.**

For one thing, `csv` provides no essential capabilities that you can't
trivially achieve with Python's built-in `str` class.

More importantly, the point of this assignment is to teach you how to process
data *generally*.  The `csv` module won't teach you how to solve problems when
your data comes in a different format than CSV.  Put another way, CSV is a
subset of plain text data.  If you know how to deal with plain text you can
deal with CSV, but the converse isn't necessarily true.  You limit yourself if
you are only able to solve problems when somebody has already written a module.

Be more than a consoomer; become the kind of programmer who *makes* the modules.
