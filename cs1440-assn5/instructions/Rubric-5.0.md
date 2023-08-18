# CS 1440 Assignment 5.0: Refactoring - Rubric

| Points | Criteria
|:------:|--------------------------------------------------------------------------------
| 25 pts | Software Development Plan is comprehensive and well-written<br/>Follows DuckieCorp project conventions
| 5 pts  | Signature file is complete
| 10 pts | 11 different code smells (one of each type) cataloged in `doc/Smells.md`<br/>Each piece of required information is included: location, code snippet, explanation and fix description
| 5 pts  | User's Manual explains the program's user interface<br/>Is written for a non-technical audience using simple terms<br/>Avoids describing internal details about how the program works
| 15 pts | UML class diagram describes your design<br/>Class diagram adheres to UML standards as far as these were explained in class<br/>All modules/classes are represented, behaviors and data members are accounted for, and relationships between modules are described
| 15 pts | Increase coverage of unit tests to eight (8) tests<br/>All unit tests pass<br/>No trivial unit tests are present
| 15 pts | Implementation: the original user interface functionality is preserved<br/>No new features or capabilities are added to the refactored program
| 20 pts | Implementation: Program requirements are met<br/>The new code is cleaner than the original starter code<br/>No code smells from the starter code are in the final product, nor are any other notable code smells added

**Total points: 110**


## Penalties

*Please read the "How To Submit Assignments" page of Canvas (found under the DuckieCorp Employee Handbook Module) for more information on these penalties and what we expect.*

***Penalties for this assignment***:

0.  **110 point penalty** if your program imports any modules **except**:
    *   `colour`
    *   `math`
    *   `sys`
    *   `time`
    *   `tkinter`
    *   `typing`
    *   `unittest`
    *   modules provided in the starter code
    *   modules you wrote yourself
    *   modules imported by the starter code
        *   There were many extraneous modules imported by the original starter code. You may to use any of those modules **so long as they serve an actual purpose in your solution**
        *   EX: You can use `itertools` to create complex iterators, `functools` to use higher order functions, but you *cannot* use `turtle` because it serves no purpose in this program
1.  **15 point penalty**  if your UML diagram is unreadable.  Watch out for a transparent background (on Diagrams.net, click File -> Export as -> PNG..., then make sure that the option "Transparent background" is left unchecked).  Make sure that the background isn't black, as this obscures the lines connecting classes to each other.  Make sure that the file size is large enough to make the text legible, and that the colors of the diagram stand out in sharp contrast to the background.
2.  **10 point penalty** for each  _trivial_ unit test (i.e. a unit test which unconditionally passes without meaningfully testing some functionality)


***Penalties for all assignments***:

#### Project Layout
0. **10 point penalty** if the repository does not follow the Git Repository Naming Convention
1. **10 point penalty** if the submitted project is not a clone of the starter code repository
2. **10 point penalty** if required files or directories are missing, renamed, or moved from their expected location
3. **10 point penalty** if there are forbidden files and directories in the submission
4. **10 point penalty** if the `.gitignore` file is missing, corrupted, or incorrectly named
5. **Late Penalty**:
    *   \<24hrs late : 75% point cap
    *   \>=24hrs & <48hrs : 50% point cap
    *   \>=48hours : no points will be given; submissions not allowed after 48hrs


#### Modules and Functions
0. **10 point penalty** if a module fails to import due to misspelling or incorrect capitalization.
1. **10 point penalty** if the program attempts to import a module from the `src.` package; this is the result of a PyCharm misconfiguration.
2. **10 point penalty** `eval()` or a similar function is used by your program; use type constructor functions such as `int()` and `float()` instead


#### Files and Paths
0. **10 point penalty** if the program contains hard-coded paths or otherwise does not function when run from *any* CWD.  (Note: names of modules in `import` statements do not count as "hard-coded").
1. **10 point penalty** if one or more data files are not closed after being processed in *ordinary* situations.  In the event of an error your program will display an error message and immediately exit; in such cases you do not need to take special measures to close files because they will automatically be closed as your program exits.
2. **100% point penalty** if external programs are called upon to do the work.  Our customer has hired you to create a pure-Python solution, not a shell script that relies on external programs.
    - Do not use `os.system()`, `subprocess`, `pipes` or similar functions and libraries
    - Write a pure Python solution, not a script that leverages external programs


#### All Else
0. **Crashing Code Penalty**:
    * *It is your responsibility to ensure that your program will work on your grader's computer*
    *   Code that crashes and cannot be quickly & easily fixed by the grader will receive 0 points on the implementation portions of the rubric
    *   Code that crashes and CAN be quickly & easily fixed by the grader (or crashes only part of the time) will receive, at most, half-credit on the implementation portion of the rubric
1. **Misspelled Tags**:
    * The grading script relies on tags to be spelled properly, incorrectly spelled tags will lose points.
