# Recursive Web Crawler User Manual

## Setup:
Run the command `python -m pip install --user -r requirements.txt`. 
This will download the libraries you need to run this program.

## Running the Program 'WEB-CRAWLER':
You may run this program from any directory so long as you run `crawler.py`.

This program takes arguments as so: `URL [DEPTH]`
This program takes in a few arguments:
* `url`: Must be an *absolute* URL, not a *relative* URL.
  * An absolute URL consists of a scheme, usually `http://` or `https://`, followed by a hostname.
  * A relative URL is in essence, only a portion of an absolute URL. These could be missing the scheme, hostname, etc.

### Examples of Absolute URLs:
* https://google.com
* https://www.coolmathgames.com
* https://www.lingscars.com

### How to Utilize max_depth:
The optional `DEPTH` argument has a default value of 3.
The `DEPTH` is the `max_depth` and will determine how far down the rabbit-hole the web crawler will delve.

If you wish to change this you may enter in a different value like so:
`crawler.py https://google.com 6`

For example, The original URLs webpage has a depth of 0.
If `DEPTH` is set to 2, the web crawler will visit any link the webpage of the original URL supplies, 
thus going into the first rabbit-hole (the original URL being the zeroth).
From there, the web-crawler will visit the links another rabbit hole down, giving it a depth of 2.

Once the web crawler has exhausted all links at the max depth it will stop jumping in rabbit holes and report how many unique pages it visited along with some other information.

__Note__: This value must be a whole number that is greater than or equal to 0.


## Expected Output:
When the program runs correctly you can expect to see output similar to this:
```
$ python src/crawler.py https://cs.usu.edu 1
Crawling from https://cs.usu.edu to a maximum distance of 1 link
https://cs.usu.edu
    http://www.usu.edu
    http://usu.edu/azindex/
    http://usu.edu/myusu/
    https://cs.usu.edu/about/index.php
    https://cs.usu.edu/news/main-feed/2018/awards-banquet.php 
    https://engineering.usu.edu/news/main-feed/2019/a-pin.php
    https://engineering.usu.edu/news/main-feed/2019/student-awards.php
    https://cs.usu.edu/students/resources/microsoft-imagine.php
    https://cs.usu.edu/files/pdf/department-map.pdf
    https://appcamp.usu.edu
    https://cs.usu.edu/students/resources/why-comp-sci.php
    https://cs.usu.edu/employment/
    https://www.youtube.com/watch?v=CRYfNVlg4lE&feature=youtu.be
    http://a.cms.omniupdate.com/10?skin=usu&account=usu&site=Engineering_CS&action=de&path=/index.pcf
...
Visited 366 unique pages in 1.5355 seconds
```

An extra line of indentation is added when the depth is increased to allow you to easily see how far down the rabbit hole your program currently is.


## Common User Errors:
### If no arguments are supplied, the expected output will look like so:
```
$ python src/crawler.py
Error: no URL supplied

USAGE: Enter arguments like so: URL [DEPTH]
```

### Invalid URLS
If an invalid URL is supplied, the expected output will look like so:
```
$ python3 src/crawler.py cs.usu.edu   
Error: cs.usu.edu is not a valid URL.
Please only use absolute URLs with this program.
Note: Make sure the scheme is either `http` or `https`.
```

### Invalid Arguments and Too Many Arguments:
If invalid arguments are given after the `url` and `max_depth`, the program will simply ignore them. Thus, the output of the given arguments should look like so:
```
$ python3 src/crawler.py https://cs.usu.edu 0 blarg just gimme a lil' glitch ' b@by
Crawling from https://cs.usu.edu to a maximum depth of 0 links
https://cs.usu.edu
Visited 1 unique pages in 0.20 seconds.
```

### Invalid Max Depth
If invalid arguments are given for the `max_depth` the program will print an error message and continue to run with the default setting.
Expected Output:
```
$ python3 src/crawler.py https://cs.usu.edu 1.2                                    
Error: invalid literal for int() with base 10: '1.2'
Make sure the argument after the URL is a positive whole number.
Setting max depth to the default value 3...
Crawling from https://cs.usu.edu to a maximum depth of 3 links
https://cs.usu.edu
    https://www.usu.edu/privacy/
        https://www.usu.edu/apply/
            https://www.usu.edu/visit/
            https://www.usu.edu/advancement/
            https://www.usu.edu/calendar/
            --- Omitted For Brevity ---
```

### Invalid First Argument:
Since all invalid arguments after URL and max depth are established are ignored, the only invalid argument could be the first and second one.
This program will assume the first argument given is a URL, thus if the first argument is invalid, the Invalid URLs error will be displayed. (Please see above)
This program will also assume the second argument given is the max depth. Thus, if the second argument is invalid, the invalid max depth error will be displayed.
