# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

This program will take standardized configuration files that the user inputs and make an image based on the information.

User will input files via the command line.

The files within this program will take advantage of object-oriented programming and abstract classes to create fractals.
This is to allow for a program that is easy to adapt and upgrade if needed.

There will be a few different classes. I will list the main ones.
* `Fractal` - The blueprint for more concrete fractal sub-classes.
* `Palette` - The blueprint for more concrete palette sub-classes.
* `main` - takes the file in a shoots its info to the right methods.


This program aims to allow standardized files to be input so more fractals can be created.
This makes the program more user-friendly and allows it to be more agile and malleable in the future.
A good solution would have many classes that modularize the code and allow for duck-typing so the code can be simple and clean.

I already know the basics of how fractals work and have a basic knowledge of abstraction and polymorphism.
This info will help me out as I implement many classes.
I also know how to parse information from a file that the user inputs.
I can foresee challenges when it comes to making palettes and checking for errors.
There are a lot more moving parts in this program so there are a lot more places an error could occur.
I will make sure to allow plenty of time for de-bugging to hopefully catch anything that could go wrong and think of 
many ways the user could try to mess up the program.


## Phase 1: System Analysis *(10%)*

**Deliver:**

This program uses a configuration file that is given as input by a user from the command line.
A standard configuration file will include this information:
* type of fractal
* centerX
* centerY
* axisLength
* pixels
* iterations
And occasionally an optional piece of info:
* creal and cimag (these must be included when the type of fractal is some variation of the Julia formula.)


The output will take the form of stderr messages to the terminal as well as images that are created.


There will be quite a few algorithms used:
* Palette will be created using a simple algorithm that alters between some color and black to create unique and interesting palettes.
* Fractals will use different mathematical algorithms to create the images. These will vary but will be somewhat similar.
* ImagePainter will use some math to place pixels on the screen correctly, it's nothing too complicated though.


## Phase 2: Design *(30%)*

**Deliver:**

#### Classes:
**FractalParser**
methods:
parse(file, image_name)
* Takes a file and turns its information into a dictionary for FractalFactory and PaletteFactory to use. The basic idea is that of a 'json decoder'.
* Raises an error when the provided file doesn't fit the standard format.

The dictionary could look something like this after all the info is parsed:
`{
    type of fractal: ~~~
    pixels: ~~~
    axisLength: ~~~
    iterations: ~~~
    min: {x: ~~~, y: ~~~}
    max: {x: ~~~, y: ~~~}
    pixelsize: ~~~
    imagename: ~~~
    *creal: ~~~
    *cimag: ~~~
}`


**FractalFactory**
methods:
main()
* returns a concrete fractal object when given information from FractalParser. This class basically takes a blueprint and shoots out a fractal.
* This doesn't necessarily need to be a class, it can just be a function within the `main` module.
* This method will have a `default` fractal that it makes if no arguments are given. This can be hard-coded into the program.
* Errors will occur when invalid configuration files are given. This will raise different errors based on what went wrong.



**PaletteFactory**
methods:
main()
* returns a concrete palette object when given information from FractalParser.
* This doesn't necessarily need to be a class. It could be a function within the `main` module.
* When no palette is specified this makes a default palette for the fractal.


**Fractal**
**Abstract Class** **3 concrete subclasses**
methods:
* count(complex number)


**Mandelbrot**
methods:
* count(complex number) -> int (this return the iterations before `formula > 2`)


**Phoenix**
methods:
* count(complex number) -> int (this return the iterations before `formula > 2`)


**Palette**
**Abstract Class** **2 concrete subclasses**
methods:
getColor()
* Takes an integer as input and returns a string which represents a color in this format: `#RRGGBB`


**ImagePainter**
methods:
* imports tkinter module (only file that is allowed to)
* Takes the products of FractalFactory, PaletteFactory and FractalParser as input
* Relies on Duck-typing to treat all `Fractal` objects the same way.



## Phase 3: Implementation *(15%)*


## Phase 4: Testing & Debugging *(30%)*

Unit tests:
* Tests the first color of each palette to make sure it is correct.
* Tests to ensure that the count() function of the fractals is behaving correctly.
* Tests to ensure that the Palette and Fractal classes are actually abstract.
* Tests the Mandelbrot and Phoenix fractals to make sure they are getting the right iterations at certain points

```
python3 src/main.py data/glooob.manfrotto
Traceback (most recent call last):
  File "/Users/justinherzog/Desktop/CS1440-Fa2022/cs1440-assn5/src/main.py", line 97, in <module>
    file = open(sys.argv[1])
           ^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'data/glooob.manfrotto'
```
Made sure an invalid file name would not open. It does just as expected.

```
python3 src/main.py data/invalid.frac    
Traceback (most recent call last):
  File "/Users/justinherzog/Desktop/CS1440-Fa2022/cs1440-assn5/src/main.py", line 98, in <module>
    fractal_info = FractalParser.parse(file, sys.argv[1])
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/justinherzog/Desktop/CS1440-Fa2022/cs1440-assn5/src/FractalParser.py", line 44, in parse
    raise RuntimeError("ERROR: The file did not provide the 'creal' data field.\nExiting Program...")
RuntimeError: ERROR: The file did not provide the 'creal' data field.
Exiting Program...

```
Error messages show up when a file is missing required information and gives the user a detailed description.

```
python3 src/main.py data/invalid.frac rainbow
ERROR: rainbow is not a valid palette
Please choose one of the following:
ocean
sunset
forest
```
Error messages show up when an invalid palette is chosen and lets the user know what the valid choices are.


## Phase 5: Deployment *(5%)*


## Phase 6: Maintenance

**Deliver:**

I think the sloppily written parts of my program are the 'ImagePainter' and 'main' files. They are just a bit more
confusing to understand than I would like. They are not over the top too confusing though.
* I know why everything in the program works except for the magic formulas for the fractals, but that's a bit above my pay grade haha.
* It would not take long to find the cause of a bug. All the files are very small and for the most part self-explanatory.

My documentation should make sense to most people.  I know it would definitely help me understand what I was doing 6 months from now.

It would be fairly easy to add a new feature to this program in a year. This is because of the awesome abstraction and polymorphism at play!

The program should continue to work with upgraded OS and hardware. Even into the next version of python. The only thing
that might break my program is the imported colour module. I don't know if the developers of it plan to keep it the same.
