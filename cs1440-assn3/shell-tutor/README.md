# CS 1440 Assignment 3: Big Data Processing - Shell Tutor Lessons

## Table Of Contents
*   [Quickstart](#quickstart)
*   [Submission Instructions](#submission-instructions)
*   [Lesson Contents](#lesson-contents)
*   [Hints](#hints)
*   [Reporting Bugs](#reporting-bugs)


## Quickstart

*In the code examples below a dollar sign `$` represents the shell prompt.  This is to distinguish commands that you will input from their output. Do not type the `$` when you run these commands yourself. Output may be replaced by `...` to shorten these instructions.*

0.  Clone this repository and set up the remotes properly, according to the instructions in the [project root README.md](../)
1.  Use `cd` to enter the `shell-tutor` directory in this repository
    ```
    $ pwd
    .../cs1440-assn3
    $ cd shell-tutor
    $ pwd
    .../cs1440-assn3/shell-tutor
    ```
2.  Execute one of the `.sh` files from Bash or Zsh
    ```
    $ ./0-tagging.sh
    Git Tag Syntax
    Tutor:
    Tutor: In this lesson you will learn how to
    Tutor:
    Tutor: * Use the basic command syntax and concepts for git tagging
    Tutor: * Add new tags to commits
    Tutor: * Remove tags from commits
    Tutor: * Manage tags on remote repositories
    ```
    *   **NOTE FOR UBUNTU USERS:** Your shell's default `sh` is not compatible with the shell tutor. You will have to launch the shell tutor lessons by typing `bash ./0-tagging.sh` instead of just `./0-tagging.sh`.


## Submission Instructions

After you finish the lessons, run `./make-certificate.sh` to make `certificate.txt` in this directory.  Then `git add`, `git commit`, and `git push` this file so it can be graded.


## Lesson Contents

*   `0-tagging.sh`
    * Learn the basic command syntax and concepts for git tagging
    * Add new tags to commits
    * Remove tags from commits
    * Manage tags on remote repositories
*   `1-project-tags.sh`
    * Add development phase tags to commits in a project
    * Push tags to remote repository


## Hints

*   Interact with the tutor through the `tutor` command.
    *   When you get lost or forget what to do next, run `tutor hint`.
*   You can leave the tutorial early by exiting the shell.  There are many
    ways to do this:
    *   The `exit` command
    *   The `tutor quit` command
    *   Type the End-Of-File character (EOF) `Ctrl-D`
*   Lessons are designed to be brief; the average student will finish a lesson
    in 20 minutes.  If you are stuck longer than 20 minutes you can seek help
    from the instructor, TAs or CS Coaching Center.


## Reporting Bugs
*   When you encounter a problem with a lesson, please send a bug report so I can fix it
    *   Run `tutor bug` 
        *   Scroll up a before the problem started and copy the text on your terminal, including these details:
        -   Which lesson you are running
        -   Which step of the lesson you were on
        -   The instructions for that step
        -   The command you ran
        -   The erroneous output
        -   The output of the `tutor bug` command
*   Send this text to me in an email: `erik DOT falor AT usu DOT edu`
    *   **Do not** send screenshots; plain text is much easier to work with
    *   **CC Jaxton Winder on the email as well** : `jaxton DOT winder AT usu DOT edu`
