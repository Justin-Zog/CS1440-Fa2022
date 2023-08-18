# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

This program will intake a URL from the user and visit URL after URL until either the time expires, or the desired depth is hit.
It will ignore links that have already been visited as well as links that go to a fragment of an already visited page.

The program can achieve this by using a recursive function that looks for links and visits them.
It would also keep track of any link it has visited so no duplicate visits are made.

The hardest part about this program will be checking for exceptions and really testing and debugging.
The internet is a wild place and you never know what you may find or what kind of weird errors we will run into.


## Phase 1: System Analysis *(10%)*

**Deliver:**

The data used by the program will be a URL. It could also possibly use a max_depth and max_time.
These will be arguments provided by the user, or default values.

The output will take the form of text printed onto the terminal as links are visited.

An algorithm to check if URLs are valid as well as to visit URLs will need to be made.


## Phase 2: Design *(30%)*

**Deliver:**

#### crawl
A recursive function that takes in a URL, maximum depth, maximum runtime, current depth, and visited sites.

* This is pretty much the only function of the program. It will check the depth of recursion and stop running when it has gone deep enough.
* It will print each URL it visits at a special level of indentation that represents the depth of which it visited the link.
* When an error is hit, it will handle it gracefully by letting the user know the link didn't work or whatever else happened
then continue with its day
* It will also be able to create an absolute address path from a relative URL if it runs into one, and remove Fragments from URLs to see if the website was already visited.
* It will return a string (the URL it visited or the exception for why it couldn't visit a link.)

```
def crawl(url, current_depth, visited, maximum_runtime=3, maximum_depth=3):
    Check the level of recursion
    Print the URL it is on with the current level of recursion
    Handle any exception that may occur from trying to visit URLs
    Create an absolute address.
    Visit the URLs it hits.
    Keeps track of the URLs it has tried to visit.
    Call itself to make the recursive magic work.
```

#### main
This function just takes in arguments from the command line and makes sure that's all good and dandy.
After that it calls the `crawl` function and kicks the program off.


## Phase 3: Implementation *(15%)*

**Deliver:**

## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

## Common User Errors:
### If no arguments are supplied, the expected output will look like so:
```
$ python src/crawler.py
Error: no URL supplied

USAGE: Enter arguments like so: url [-d DEPTH] [-t TIME] 
```

### Invalid URLS
If an invalid URL is supplied, the expected output will look like so:
```
$ python src/crawler.py cs.usu.edu
Error: cs.usu.edu is not a valid URL.
Please only use absolute URLs with this program.
```

### Invalid Arguments and Too Many Arguments:
If invalid arguments are given after the url, the program will simply ignore them. Thus, the output of the given arguments should look like so:
```
$ python src/crawler.py https://cs.usu.edu blarg, this isn't -d 0 suppose to -t 3 be here 
Crawling from https://cs.usu.edu to a maximum distance of 0 links
https://cs.usu.edu
Visited 1 unique page in 0.2057 seconds
```

### Invalid Max Depth or Max Time
If invalid arguments are given for the `max_depth` or `max_runtime`, the program will print an error message and continue to run with the default setting.
Expected Output:
```
python3 src/crawler.py https://cs.usu.edu -d -6.7 -t 3.8982
Error: invalid literal for int() with base 10: '-6.7'
The argument after `-d` must be a whole number greater than or equal to 0.
Error: invalid literal for int() with base 10: '3.8982'
The argument after `-t` must be a whole number greater than or equal to 0.
Crawling from https://cs.usu.edu to a maximum depth of 3 links
https://cs.usu.edu
    https://www.usu.edu/privacy/
        https://www.usu.edu/apply/
            https://www.usu.edu/visit/
            https://www.usu.edu/advancement/
            ... --- Omitted to save space ---
            https://catalog.usu.edu/
            https://catalog.usu.edu/content.php?catoid=12&navoid=3320
Visited 43 unique pages in 10.01 seconds.
```

### Invalid First Argument:
Since all invalid arguments after the URL is established are ignored, the only invalid argument could be the first one.
This program will assume the first argument given is a URL, thus if the first argument is invalid, the Invalid URLs error will be displayed. (Please see above)

## Phase 5: Deployment *(5%)*

**Deliver:**

## Phase 6: Maintenance

**Deliver:**

Most of the program is actually written in a clean manner. The only part that gets a little messy is checking the links in the html to see if they are valid and what not.
If a bug was reported in a few months it would not take me long to find it. Especially with how short the program is.

My documentation should make sense to myself and others who read it in the future.
I try to keep things simply and state what the program is suppose to do, that way people can look at my code and decide if they want to implement it differently
since they should have an understanding of the big picture.

It would be very easy to add a new feature in the future. I'm very tempted to add a few already.  The code is very small and creating a new feature would not take long at all.

This program should work in the future. However it may have to be updated to use the latest version of Python's url parser or BeautifulSoup
